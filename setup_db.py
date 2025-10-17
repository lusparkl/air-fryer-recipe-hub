from app.scrapers._scrape_helpers import get_suitable_links, scrape_recipe_based_on_source
from app.db.crud import RecipesManager

def main():
    db = RecipesManager()
    
    links_and_sources = get_suitable_links()
    for link_and_source in links_and_sources:
        try:
            recipe = scrape_recipe_based_on_source(url_and_source=link_and_source)
            db.add_recipe(recipe=recipe)
        except (IndexError, ValueError, AttributeError):
            continue
   

if __name__ == "__main__":
    main()