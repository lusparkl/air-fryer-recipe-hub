from app.scrapers.seriouseats import SeriousEats
import pytest

@pytest.fixture
def recipe():
    return SeriousEats(url="https://www.seriouseats.com/air-fried-southern-fried-chicken-recipe-11801085?advertest=myrecipes&_gl=1*72mgsw*_ga*NzgzNjQwNzg5LjE3NTk0MjM4Njk.*_ga_DK3GDWHWJH*czE3NjA0MTI2MDMkbzE4JGcxJHQxNzYwNDEzNDAyJGo1JGwwJGgw")

def test_get_name(recipe):
    assert recipe.name == "My Foolproof, Fast Way to Crispy, Juicy “Fried” Chicken (Without Deep Frying)"

def test_get_description(recipe):
    assert recipe.description == 'A buttermilk-pickle brine and a well-seasoned dredge work together with the air fryer for this quick, easy, and fantastically juicy and crispy "fried" chicken.'

def test_get_time_details(recipe):
    assert recipe.prep_time == 15
    assert recipe.overall_time == 305

def test_get_nutrion_facts(recipe):
    assert recipe.calories == 633
    assert recipe.fat ==26
    assert recipe.carbs == 60
    assert recipe.protein == 40

def test_get_ingridients(recipe):
    assert recipe.ingridients == ["2 cups (480 ml) whole buttermilk", "2 large eggs", "1/4 cup (60 ml) dill pickle brine, drained from 1 jar of pickles, plus pickle slices for serving", "2 tablespoons (30 ml)Louisiana-style hot sauce (such as Crystal)", "2 tablespoons (30 ml)honey", "4 tablespoons (36 g) Diamond Crystal kosher salt, divided, plus more to taste; for table salt, use half as much by volume or same weight", "4 small bone-in, skin-on chicken thighs (5 to 7 ounces; 141 to 198 g each)",
                                  "2 medium bone-in, skin-on chicken breast halves (about 1 pound; 454 g each)", "1 1/2 cups all purpose flour (6 3/4 ounces; 192 g)", "1 cup white rice flour (about 5 1/4 ounces; 150 g), see note", "1 tablespoon onion powder", "1 tablespoon granulated garlic", "2 teaspoons smoked paprika", "1 1/2 teaspoons baking powder", "1 teaspoon freshly ground black pepper", "2 tablespoons (30 ml) canola oil, divided", "Cooking spray"]

def test_get_img(recipe):
    assert recipe.img == "https://www.seriouseats.com/thmb/rW8rE9g_0PbdZPLzqMczvQ0MfLk=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/20240520Serious-Eats-AirFryerSouthernFriedChicken-Causey-HERO-dcd71aa2b7e145699e2559abb20d76cf.jpg"