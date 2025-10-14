from app.scrapers.simplyrecipes import SimplyRecipies
import pytest

@pytest.fixture
def recipe():
    return SimplyRecipies(url="https://www.simplyrecipes.com/air-fryer-potato-chip-chicken-tenders-recipe-11678667?advertest=myrecipes&_gl=1*3pyp38*_ga*NzgzNjQwNzg5LjE3NTk0MjM4Njk.*_ga_DK3GDWHWJH*czE3NjA0Mzc2NjQkbzE5JGcxJHQxNzYwNDM4NzI2JGo2MCRsMCRoMA..")

def test_get_name(recipe):
    assert recipe.name == "The Secret to No-Mess “Fried” Chicken Is in the Snack Aisle"

def test_get_description(recipe):
    assert recipe.description == 'A coating of crushed potato chips makes these air-fried chicken tenders ultra-crispy—no deep frying required.'

def test_get_time_details(recipe):
    assert recipe.prep_time == 30
    assert recipe.overall_time == 50

def test_get_nutrion_facts(recipe):
    assert recipe.calories == 656
    assert recipe.fat == 30
    assert recipe.carbs == 35
    assert recipe.protein == 59

def test_get_ingridients(recipe):
    assert recipe.ingridients == ["1 cup all-purpose flour", "2 tablespoons seasoned salt (such as Lawry’s)", "1 teaspoon freshly ground black pepper", "3 large eggs, lightly beaten", "1 (13-ounce) bag kettle-cooked potato chips", "2 pounds boneless, skinless chicken tenders (about 12)", "1 teaspoon kosher salt, plus more to taste", "Nonstick cooking spray"]

def test_get_img(recipe):
    assert recipe.img == "https://www.simplyrecipes.com/thmb/mbGI_EKp-S9ZD5VAQTntW23tAfQ=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/simply-recipes-air-fryer-chicken-tenders-lead-3-ef50aa06270c41ac8d26c90600d9d8cb.jpg"