import sqlite3
from typing import List
import json


def connect():
    """
    Connect to the database and return the connection and cursor
    """

    conn = sqlite3.connect("data/recipes.db")
    c = conn.cursor()
    print("Connected to the database")
    return conn, c


def close(conn):
    """
    Close the connection to the database
    """

    conn.close()


def match_recipe(
    ingredients: List, boolean_operations: List, limit: int, connection, cursor
):
    """
    Match the recipes with the given ingredients and boolean operations in between the ingredients
    """

    # Create the query
    query = "SELECT name, ingredients, instructions FROM recipes WHERE "

    for i, ingredient in enumerate(ingredients):
        query += f"ingredients LIKE '%{ingredient}%'"

        if i < len(boolean_operations):
            query += f" {boolean_operations[i]} "

    query += f" LIMIT {limit}"

    # Execute the query
    cursor.execute(query)
    results = cursor.fetchall()

    return results


if __name__ == "__main__":
    conn, c = connect()
    res = match_recipe(["tomato", "onion"], ["AND"], 1, conn, c)
    for r in res:
        print(r[0])
        print(list(json.loads(r[1])))
        print(list(json.loads(r[2])))
    close(conn)
