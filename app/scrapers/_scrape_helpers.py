from selenium import webdriver
from bs4 import BeautifulSoup
import time
from app.scrapers.allrecipes import AllRecipes
from app.scrapers.eatingwell import EatingWell
from app.scrapers.seriouseats import SeriousEats
from app.scrapers.simplyrecipes import SimplyRecipies
from app.scrapers.spruceeats import SpruceEats

BASE_LINK = "https://www.myrecipes.com/search?q=air+fryer&offset="
SUITABLE_WEBSITES = ["Allrecipes", "The Spruce Eats", "EatingWell", "Simply Recipes", "Serious Eats"]
options = webdriver.FirefoxOptions()
options.add_argument("--headless")
browser = webdriver.Firefox(options=options)

def get_suitable_links(*, link: str = BASE_LINK, suitable_websites: list = SUITABLE_WEBSITES, MAX_OFFSET: int = 1000000) -> list:
    links_and_sources = []
    recipes_quantity = 24
    offset = 0
    max_retries = 3
    
    while recipes_quantity == 24 and offset <= MAX_OFFSET:
        for attempt in range(max_retries):
            try:
                # Set page load timeout to 30 seconds
                browser.set_page_load_timeout(30)
                browser.get(url=f"https://www.myrecipes.com/search?q=air+fryer&offset={offset}")
                time.sleep(5)
                html = browser.page_source
                soup = BeautifulSoup(html, "lxml")
                
                recipes_list = soup.find_all("a", class_="search-results-card__link")
                recipes_quantity = len(recipes_list)

                # Process recipes only if we successfully loaded the page
                for recipe in recipes_list:
                    url = recipe.attrs["href"]
                    from_site = recipe.find("span", class_="search-results-card__brand-name").text

                    if from_site in suitable_websites:
                        links_and_sources.append((url, from_site))
                
                # If successful, break the retry loop
                break
            
            except Exception as e:
                print(f"Attempt {attempt + 1} failed: {str(e)}")
                if attempt == max_retries - 1:
                    print(f"Failed to load page at offset {offset} after {max_retries} attempts")
                    # If all retries failed, consider this page empty
                    recipes_quantity = 0
                    break
                time.sleep(10)  # Wait longer between retries
        
        offset += 24
        
    # Clean up browser at the end
    try:
        browser.quit()
    except:
        pass
        
    return links_and_sources

def scrape_recipe_based_on_source(*, url_and_source: tuple):
    url, source = url_and_source
    
    match source:
        case "Allrecipes":
            return AllRecipes(url=url)
        case "The Spruce Eats":
            return SpruceEats(url=url)
        case "EatingWell":
            return EatingWell(url=url)
        case "Simply Recipes":
            return SimplyRecipies(url=url)
        case "Serious Eats":
            return SeriousEats(url=url)
        case _:
            raise ValueError("Website from unsuitable source")
