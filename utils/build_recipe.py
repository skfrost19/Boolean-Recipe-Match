import sqlite3
import os
import json


def create_db():
    conn = sqlite3.connect("data/recipes.db")
    c = conn.cursor()
    c.execute("CREATE TABLE recipes (name TEXT, ingredients TEXT, instructions TEXT)")
    conn.commit()
    conn.close()


def insert_data():
    conn = sqlite3.connect("data/recipes.db")
    c = conn.cursor()
    with open("data/recipes.json") as f:
        recipes = json.load(f)
    for recipe in recipes:
        ingredients_json = json.dumps(recipe["Ingredients"])
        method_json = json.dumps(recipe["Method"])
        c.execute(
            "INSERT INTO recipes VALUES (?, ?, ?)",
            (recipe["Name"], ingredients_json, method_json),
        )
    conn.commit()
    conn.close()


def dump_db():
    os.system("sqlite3 recipes.db .dump > recipes.sql")
    os.system("mv recipes.sql recipes/")
    os.system("rm recipes.db")


if __name__ == "__main__":
    create_db()
    insert_data()
    # dump_db()
