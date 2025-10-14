from app.scrapers.eatingwell import EatingWell
import pytest

@pytest.fixture
def recipe():
    return EatingWell(url="https://www.eatingwell.com/recipe/270404/crispy-air-fryer-french-fries/?advertest=myrecipes&_gl=1*qxyqxp*_ga*NzgzNjQwNzg5LjE3NTk0MjM4Njk.*_ga_DK3GDWHWJH*czE3NjA0MTI2MDMkbzE4JGcxJHQxNzYwNDEyNjEzJGo1MCRsMCRoMA..")

def test_get_name(recipe):
    assert recipe.name == "Crispy Air-Fryer French Fries"

def test_get_description(recipe):
    assert recipe.description == "Get crispy, crunchy fries with much less oil than deep frying requires with these air-fried spuds. For the best texture, keep each fry as evenly sized as possible. Try a mandoline to make quick work of equal fries if your knife work could use some help."

def test_get_time_details(recipe):
    assert recipe.prep_time == 30
    assert recipe.overall_time == 60

def test_get_nutrion_facts(recipe):
    assert recipe.calories == 185
    assert recipe.fat ==10
    assert recipe.carbs == 23
    assert recipe.protein == 3

def test_get_ingridients(recipe):
    assert recipe.ingridients == ["2 (6 ounce) russet baking potatoes", "2 tablespoons olive oil", "1 tablespoon cornstarch", "½ teaspoon coarsely cracked black pepper", "⅜ teaspoon salt", "¼ teaspoon paprika", "Cooking spray"]

def test_get_directions(recipe):
    assert recipe.directions == ["Scrub potatoes well. Cut the unpeeled potatoes lengthwise into 3/8-inch sticks. Place in a large bowl; cover with water and let stand for 30 minutes. Drain well and pat very dry. Return to the dried bowl; add oil and toss to coat. Sprinkle with cornstarch, pepper, salt and paprika; toss to coat.",
                                 "Coat the basket of an air fryer with cooking spray. Place the potatoes in the basket and coat the potatoes well with cooking spray. Fry at 360 degrees F, stirring every 5 minutes, until very crispy, 25 to 30 minutes."]

def test_get_img(recipe):
    assert recipe.img == "https://www.eatingwell.com/thmb/DzBXw2-6To3m-z6zGSQSMvysZdE=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/6318342-1656df4b08ab465e9f6e0da9b7906daf.jpg"