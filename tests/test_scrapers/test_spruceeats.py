from app.scrapers.spruceeats import SpruceEats
import pytest

@pytest.fixture
def recipe():
    return SpruceEats(url="https://www.thespruceeats.com/air-fryer-asparagus-recipe-5179953?advertest=myrecipes&_gl=1*2m144u*_ga*NzgzNjQwNzg5LjE3NTk0MjM4Njk.*_ga_DK3GDWHWJH*czE3NjA0Mzc2NjQkbzE5JGcxJHQxNzYwNDM5Mjc3JGo1MiRsMCRoMA..")

def test_get_name(recipe):
    assert recipe.name == "Air Fryer Asparagus"

def test_get_description(recipe):
    assert recipe.description == 'With Lemon and Parmesan Cheese'

def test_get_time_details(recipe):
    assert recipe.prep_time == 8
    assert recipe.overall_time == 20

def test_get_nutrion_facts(recipe):
    assert recipe.calories == 62
    assert recipe.fat == 4
    assert recipe.carbs == 6
    assert recipe.protein == 4

def test_get_ingridients(recipe):
    assert recipe.ingridients == ["1 to 1 1/2 pounds asparagus", "1 tablespoon olive oil", "1/2 teaspoon garlic powder", "1/4 teaspoon kosher salt, or to taste", "1/4 teaspoon freshly ground black pepper, or to taste", "1 tablespoon lemon juice", "4 tablespoons grated Parmesan cheese, for garnish and serving"]

def test_get_img(recipe):
    assert recipe.img == "https://www.thespruceeats.com/thmb/mi_tXx_5qW9dj8EMQPTAoGyieeo=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/air-fryer-asparagus-recipe-5179953-6-aec158b8bf9349be928bfbce69a11bc9.jpg"