from app.scrapers._abstract import Abstract_scraper
from app.scrapers._utils import nutrion_facts_to_int, pretiffy_strings_list, time_details_in_minutes
from app.ai.api_client import get_recipe_categories

class SpruceEats(Abstract_scraper):
    def get_name(self):
        return self.soup.find("h1", class_ = "heading__title").text.strip()

    def get_description(self):
        return self.soup.find("p", class_ = "heading__subtitle").text.strip()
    
    def get_time_details(self):
        recipe_time_details = self.soup.find("div", class_ = "project-meta__times-container")
        all_time_data = recipe_time_details.find_all("span", class_ = "meta-text__data")
        prep_time = all_time_data[0].text
        if len(all_time_data) == 3:
            overall_time = all_time_data[2].text
        elif len(all_time_data) == 4:
            overall_time = all_time_data[3].text
        else:
            raise ValueError("Didn't expect this quantity of time data about recipe")
        
        return time_details_in_minutes([prep_time, overall_time])

    def get_nutrion_facts(self):
        nutrion_facts = self.soup.find_all("tr", class_ = "nutrition-info__table--row")
        calories = nutrion_facts_to_int(nutrion_facts[0].find("td", class_ = "nutrition-info__table--cell").text)
        fat = nutrion_facts_to_int(nutrion_facts[1].find("td", class_ = "nutrition-info__table--cell").text)
        carbs = nutrion_facts_to_int(nutrion_facts[2].find("td", class_ = "nutrition-info__table--cell").text)
        protein = nutrion_facts_to_int(nutrion_facts[3].find("td", class_ = "nutrition-info__table--cell").text)

        return [calories, fat, carbs, protein]

    def get_ingridients(self):
        ingridients_raw = self.soup.find_all("li", class_ = "structured-ingredients__list-item")
        
        return pretiffy_strings_list(ingridients_raw)

    def get_directions(self):
        directions_container = self.soup.find("ol", class_ = "comp mntl-sc-block mntl-sc-block-startgroup mntl-sc-block-group--OL")
        directions_raw = directions_container.find_all("p", class_ = "comp mntl-sc-block mntl-sc-block-html")

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