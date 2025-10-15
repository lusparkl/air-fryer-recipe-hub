from google import genai
from google.genai import types
from app.ai.config import GEMINI_API_KEY, instruction
import json

client = genai.Client(api_key=GEMINI_API_KEY)

def get_recipe_categories(*, recipe_name: str, ingridients: list) -> list:
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        config=types.GenerateContentConfig(
            system_instruction=instruction),
        contents=f"Recipe name: {recipe_name}, Ingredients: {ingridients}"
    )
    return json.loads(response.text)