# filepath: app/db/crud.py
from app.db.base import Session, Base, engine
from app.db.models import Recipe
from app.scrapers._abstract import Abstract_scraper



class RecipesManager:
    def __init__(self):
        Base.metadata.create_all(bind=engine)
        self.session_factory = Session

    def add_recipe(self, *, recipe: Abstract_scraper):
        with self.session_factory() as db:
            new_recipe = Recipe(name=recipe.name, description=recipe.description, prep_time=recipe.prep_time, overall_time=recipe.overall_time,
                                 calories=recipe.calories, fat=recipe.fat, carbs=recipe.carbs, protein=recipe.protein, ingridients=recipe.ingridients,
                                 directions=recipe.directions, image=recipe.img, categories=recipe.categories)
            responce = db.add(new_recipe)
            db.commit()
            return responce

    def get_recipe(self, recipe_id: int):
        with self.session_factory() as db:
            return db.query(Recipe).filter(Recipe.id == recipe_id).first()

    def delete_recipe(self, recipe_id: int):
        with self.session_factory() as db:
            recipe = self.get_recipe(recipe_id)
            if recipe:
                responce = db.delete(recipe)
                db.commit()
                return responce
