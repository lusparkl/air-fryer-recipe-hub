from bs4 import BeautifulSoup
import requests
from ._utils import headers

class Abstract_scraper():
    def __init__(self, url):
        html_text = requests.get(url, headers=headers).text
        self.soup = BeautifulSoup(html_text, "lxml")
        
        self.name = self.get_name()
        self.description = self.get_description()
        self.prep_time, self.overall_time = self.get_time_details()
        self.calories, self.fat, self.carbs, self.protein = self.get_nutrion_facts()
        self.ingridients = self.get_ingridients()
        self.directions = self.get_directions()
        self.img = self.get_img()

    def get_name(self):
        raise NotImplementedError("this should be implemented")

    def get_description(self):
        raise NotImplementedError("this should be implemented")
    
    def get_time_details(self):
        raise NotImplementedError("this should be implemented")

    def get_nutrion_facts(self):
        raise NotImplementedError("this should be implemented")

    def get_ingridients(self):
        raise NotImplementedError("this should be implemented")

    def get_direcitons(self):
        raise NotImplementedError("this should be implemented")

    def get_img(self):
        raise NotImplementedError("this should be implemented")
