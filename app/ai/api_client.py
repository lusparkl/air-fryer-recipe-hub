from openai import OpenAI
from app.ai.config import OPENAI_API_KEY, instruction, model
import json
client = OpenAI(api_key=OPENAI_API_KEY)



def get_recipe_categories(*, recipe_name: str, ingridients: list) -> list:
    response = client.responses.create(
        model=model,
        instructions=instruction,
        input=f"Recipe name: {recipe_name}, Ingredients: {ingridients}"
    )

    return json.loads(response.output_text)