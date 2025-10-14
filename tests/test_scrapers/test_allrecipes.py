from app.scrapers.allrecipes import AllRecipes
import pytest

@pytest.fixture
def recipe():
    return AllRecipes(url="https://www.allrecipes.com/recipe/280533/air-fryer-truffle-fries/?advertest=myrecipes&_gl=1*et1t90*_ga*NzgzNjQwNzg5LjE3NTk0MjM4Njk.*_ga_DK3GDWHWJH*czE3NjAzODE5NjkkbzE3JGcxJHQxNzYwMzgyMDUwJGo1MSRsMCRoMA..")

def test_get_name(recipe):
    assert recipe.name == "Air Fryer Truffle Fries"

def test_get_description(recipe):
    assert recipe.description == "I fell in love with truffle fries from the moment I met them on my first trip to Las Vegas. I've made them often since then but finally took the time to experiment in the air fryer for a healthier alternative. These will step up your fry game..."

def test_get_time_details(recipe):
    assert recipe.prep_time == 10
    assert recipe.overall_time == 60

def test_get_nutrion_facts(recipe):
    assert recipe.calories == 226
    assert recipe.fat == 8
    assert recipe.carbs == 36
    assert recipe.protein == 5

def test_get_ingridients(recipe):
    assert recipe.ingridients == ["1 ¾ pounds russet potatoes, peeled and cut into fries", "2 tablespoons truffle-infused olive oil", "½ teaspoon paprika", "1 tablespoon grated Parmesan cheese", "2 teaspoons chopped fresh parsley", "1 teaspoon black truffle sea salt"]

def test_get_directions(recipe):
    assert recipe.directions == ["Place fries in a bowl. Cover with water and let soak for 30 minutes. Drain and pat dry.",
                                 "Preheat the air fryer to 400 degrees F (200 degrees C) according to manufacturer's instructions.",
                                 "Place drained fries into a large bowl. Add truffle olive oil and paprika; stir until evenly combined. Transfer fries to the air fryer basket.",
                                 "Air fry for 20 minutes, shaking every 5 minutes. Transfer fries to a bowl. Add Parmesan cheese, parsley, and truffle salt. Toss to coat."]

def test_get_img(recipe):
    assert recipe.img == "https://www.allrecipes.com/thmb/z8LcbLTuI5fB8XpJPigdmFvvRug=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/8198065-5bd7e28290c041ca98c12c1993c3648e.jpg"