# Todo: Add method to browse all recipes(with pagination functional)
from base import Session
from models import Recipe

class RecipesManager:
    def __init__(self):
        self.db = Session()
    
    def add_recipe(self, *, name, description, prep_time, overall_time, calories, fat, carbs, protein, ingridients, directions, image, categories):
        new_recipe = Recipe(name=name, description=description, prep_time=prep_time, overall_time=overall_time,
                             calories=calories, fat=fat, carbs=carbs, protein=protein, ingridients = ingridients,
                             directions=directions, image=image, categories=categories)
        self.db.add(new_recipe)
        self.db.commit()
    
    def get_recipe(self, recipe_id: int):
        return self.db.query(Recipe).filter(Recipe.id == recipe_id).first()
    
    def delete_recipe(self, recipe_id: int):
        recipe = self.get_recipe(recipe_id)
        if recipe:
            self.db.delete(recipe)
            self.db.commit()
    
    def __del__(self):
        self.db.close()