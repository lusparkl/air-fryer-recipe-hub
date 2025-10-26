from app.scrapers._abstract import Abstract_scraper
from app.scrapers._utils import nutrion_facts_to_int, pretiffy_strings_list, time_details_in_minutes
from app.ai.api_client import get_recipe_categories

class AllRecipes(Abstract_scraper):
    def get_name(self):
        return self.soup.find("h1", class_ = "article-heading text-headline-400").text.strip()

    def get_description(self):
        try:
            return self.soup.find("p", class_ = "article-subheading text-utility-300").text.strip()
        except AttributeError:
            return None
    
    def get_time_details(self):
        recipe_time_details = self.soup.find_all("div", class_ = "mm-recipes-details__item")
        prep_time = recipe_time_details[0].find("div", class_ = "mm-recipes-details__value").text
        if len(recipe_time_details) == 6:
            overall_time = recipe_time_details[3].find("div", class_ = "mm-recipes-details__value").text
        else:
            overall_time = recipe_time_details[2].find("div", class_ = "mm-recipes-details__value").text

        return time_details_in_minutes([prep_time, overall_time])

    def get_nutrion_facts(self):
        nutrion_facts = self.soup.find_all("td", class_ = "mm-recipes-nutrition-facts-summary__table-cell text-body-100-prominent")
        calories = nutrion_facts_to_int(nutrion_facts[0].text)
        fat = nutrion_facts_to_int(nutrion_facts[1].text)
        carbs = nutrion_facts_to_int(nutrion_facts[2].text)
        protein = nutrion_facts_to_int(nutrion_facts[3].text)

        return [calories, fat, carbs, protein]

    def get_ingridients(self):
        ingridients_raw = self.soup.find_all("li", class_ = "mm-recipes-structured-ingredients__list-item")
        return pretiffy_strings_list(ingridients_raw)

    def get_directions(self):
        directions_raw = self.soup.find_all("p", class_ = "comp mntl-sc-block mntl-sc-block-html")
        return pretiffy_strings_list(directions_raw)

    def get_recipe_categories(self):
        return get_recipe_categories(recipe_name=self.name, ingridients=self.ingridients)
    
    def get_img(self):
        try:
            image_container = self.soup.find("div", class_ = "primary-image__media")
            image = image_container.find("img")
            img = image.attrs["src"]
        except AttributeError:
            img = None
        
        return img