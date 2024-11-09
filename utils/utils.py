from typing import List
import json


def clean_recipe(recipes: List) -> List:
    """
    Clean the recipes to remove the unwanted characters
    """
    cleaned_recipes = []
    for recipe in recipes:
        cleaned_recipe = {
            "name": recipe[0],
            "ingredients": list(json.loads(recipe[1])),
            "instructions": list(json.loads(recipe[2])),
        }
        cleaned_recipes.append(cleaned_recipe)

    return cleaned_recipes
