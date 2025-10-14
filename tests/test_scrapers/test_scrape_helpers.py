from app.scrapers._scrape_helpers import get_suitable_links, scrape_recipe_based_on_source
import pytest
from app.scrapers.allrecipes import AllRecipes
from app.scrapers.eatingwell import EatingWell

links_and_sources_testdata = [(('https://www.allrecipes.com/recipe/8395452/air-fryer-frozen-french-fries/', 'Allrecipes'), AllRecipes),  (('https://www.eatingwell.com/recipe/270404/crispy-air-fryer-french-fries/', 'EatingWell'), EatingWell)]

def test_get_suitable_links():
    result = get_suitable_links(MAX_OFFSET=24)
    assert isinstance(result, list)
    assert len(result) != 0 
    
@pytest.mark.parametrize("link_and_source, expected", links_and_sources_testdata)
def test_scrape_recipe_based_on_source(link_and_source, expected):
    result = scrape_recipe_based_on_source(url_and_source=link_and_source)
    assert isinstance(result, expected)