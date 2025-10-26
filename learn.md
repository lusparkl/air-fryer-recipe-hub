# How I Built Air Fryer Recipe Hub

This is a behind‑the‑scenes walkthrough of how I put the project together: the architecture, key decisions, scraping flow, and how data moves from the web into the database with a bit of AI help.

## What this project does

- Finds air fryer recipes from major cooking sites by querying an aggregator
- Scrapes each recipe page into a consistent schema
- Normalizes and cleans fields (times, nutrition, ingredients, directions)
- Uses AI to tag recipes with 1–3 relevant categories
- Stores everything in a relational database via SQLAlchemy ORM

## Architecture at a glance

- Data model: `app/db/models.py` (SQLAlchemy ORM)
- DB session/engine: `app/db/base.py`, CRUD: `app/db/crud.py`
- Scraper interface: `app/scrapers/_abstract.py`
- Site scrapers: `app/scrapers/*.py` (AllRecipes, EatingWell, SeriousEats, SimplyRecipes, SpruceEats)
- Scraping helpers: `app/scrapers/_scrape_helpers.py` and `app/scrapers/_utils.py`
- AI categorization: `app/ai/api_client.py`, config in `app/ai/config.py`
- Orchestration/entry: `setup_db.py`

## The data model first

I started by defining the recipe shape in `app/db/models.py` so everything downstream targets the same contract:

- id (int, PK)
- name (text)
- description (nullable text)
- prep_time (minutes, int)
- overall_time (minutes, int)
- calories, fat, carbs, protein (ints)
- ingridients (JSON array of strings)
- directions (JSON array of strings)
- image (nullable text URL)
- categories (JSON array of strings)

Notes:
- I intentionally stored list‑like fields (ingredients, directions, categories) as JSON for simplicity and portability.
- The field name `ingridients` preserves the spelling used in scrapers and CRUD to keep everything aligned.

DB plumbing lives in `app/db/base.py`:
- Loads `CONNECTION_STRING` from `.env`
- Creates an `engine`, `Base` (declarative), and `Session` (sessionmaker)

Basic persistence is wrapped by `RecipesManager` in `app/db/crud.py`:
- `add_recipe(...)` maps a scraper object’s attributes into a `Recipe`
- `get_recipe(id)` and `delete_recipe(id)` provide simple accessors

## Scraping flow

I split scraping into two parts: discovery (finding recipe links) and extraction (parsing a recipe page).

### 1) Discovery via aggregator

File: `app/scrapers/_scrape_helpers.py`

- Uses headless Firefox (Selenium) to load paginated search results from MyRecipes: `https://www.myrecipes.com/search?q=air+fryer&offset=...`
- Filters results to “suitable” brands only: `Allrecipes`, `The Spruce Eats`, `EatingWell`, `Simply Recipes`, `Serious Eats`
- Returns a list of `(url, source)` tuples for downstream processing
- Includes basic retry logic, a page‑load timeout, and ensures the browser is quit at the end

Why Firefox? It’s stable headless, and the markup I needed was rendered in the static DOM. A lightweight sleep was enough without complex waits.

### 2) Extraction via site scrapers

Interface: `app/scrapers/_abstract.py`

- Fetches the recipe page with `requests` + BeautifulSoup
- Normalized methods I implement per site:
  - `get_name()`, `get_description()`
  - `get_time_details()` → returns `[prep_minutes, overall_minutes]`
  - `get_nutrion_facts()` → returns `[calories, fat, carbs, protein]`
  - `get_ingridients()` → list of strings
  - `get_directions()` → list of strings
  - `get_recipe_categories()`
  - `get_img()`

Each site module (e.g., `allrecipes.py`, `eatingwell.py`, `seriouseats.py`, `simplyrecipes.py`, `spruceeats.py`) knows its own HTML and extracts the same fields into the unified schema.

### Utilities for normalization

File: `app/scrapers/_utils.py`

- `pretiffy_strings_list(...)` cleans whitespace/newlines from lists of tags
- `nutrion_facts_to_int(...)` converts things like “12g” → 12
- `time_details_in_minutes(...)` parses human strings into minutes, handling days, hours, and minutes (e.g., “1 day 2 hrs 10 mins”)

These helpers let each scraper stay terse and consistent.

## AI categorization

File: `app/ai/api_client.py` with config in `app/ai/config.py`

- The scrapers call `get_recipe_categories(recipe_name, ingridients)`
- Behind the scenes I use the OpenAI Responses API with a strict instruction to return only a JSON array of up to 3 categories from a fixed list
- The result is parsed with `json.loads(response.output_text)` and stored into the `categories` JSON column

Environment:
- `OPENAI_API_KEY` in `.env`
- Model is set in config (small, fast model for categorization)

## Orchestration: glueing it together

File: `setup_db.py`

- Instantiate `RecipesManager` (which also ensures tables exist)
- Call `get_suitable_links()` to collect `(url, source)` pairs
- For each link, choose the right scraper via `scrape_recipe_based_on_source(...)`
- Add the parsed recipe to the DB
- Catch a few common exceptions to keep the pipeline resilient and keep going

This script is the one‑shot “ingest” runner for populating the database.

## Error handling and resilience

- Discovery uses retry/backoff for page loads and always quits the Selenium driver
- Per‑site scrapers handle optional fields (e.g., missing descriptions or images)
- The ingest loop continues on recoverable exceptions (index/attribute/value errors from unexpected markup)

## Design choices and trade‑offs

- Simplicity over generality: each site has its own scraper with explicit selectors; it’s easy to read and adjust when sites change
- JSON for list fields: avoids joining tables prematurely; keeps writes simple; can be evolved later if analytics require relational joins
- Two‑stage pipeline: discovery separated from extraction makes it easy to plug in more sources or swap discovery logic
- Headless Selenium for discovery only: actual page parsing is done with `requests` + BeautifulSoup for speed

Known rough edges to improve later:
- Field name `ingridients` is misspelled; kept consistent to avoid breaking code, but should be migrated
- README mentions Chrome WebDriver, while code uses Firefox (Gecko). The code is currently set up for Firefox headless
- Requirements include `psycopg2` (Postgres), while earlier docs said MySQL; the code is database‑agnostic via `CONNECTION_STRING` and works with whatever driver the URI targets

## How to run locally (summary)

1) Create a `.env` with at least:

```
CONNECTION_STRING=postgresql+psycopg2://user:pass@localhost:5432/airfryer
OPENAI_API_KEY=sk-...
```

2) Install dependencies:

```
pip install -r requirements.txt
```

3) Ensure you have a Firefox WebDriver (GeckoDriver) available in PATH for Selenium headless.

4) Ingest recipes:

```
python setup_db.py
```

## Testing notes

Tests live under `tests/` and cover scraper behavior and utilities. I leaned on them while tweaking selectors and normalization logic.

## What I’d do next

- Migrate `ingridients` → `ingredients` with an Alembic migration and compatibility mapping
- Add logging (structured logs, per‑URL tracing) and richer error reporting
- Deduplicate recipes by normalized URL and/or name + source key
- Add rate limiting and polite delays for requests; add retries for HTTP fetches
- Add an API (FastAPI) and simple UI to browse/search stored recipes
- Expand categorization beyond fixed labels (or learn labels from data)

## Appendix: Recipe contract (what scrapers output)

Each site scraper creates an object with the following attributes used by `RecipesManager.add_recipe(...)`:

- name: str
- description: Optional[str]
- prep_time: int (minutes)
- overall_time: int (minutes)
- calories: int
- fat: int
- carbs: int
- protein: int
- ingridients: list[str]
- directions: list[str]
- img: Optional[str] (URL)
- categories: list[str]

This is intentionally minimal but covers the most useful basics for storing and later serving recipes.
