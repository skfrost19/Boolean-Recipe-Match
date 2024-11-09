from fastapi import FastAPI, Request, Depends
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from utils.boolean_match import match_recipe, connect, close
from utils.utils import clean_recipe
from urllib.parse import parse_qs

app = FastAPI()

# connect to the database
conn, c = connect()

# models.Base.metadata.create_all(bind=database.engine)
app.mount("/static", StaticFiles(directory="app/static"), name="static")
templates = Jinja2Templates(directory="app/templates")


@app.get("/")
def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/match/")
async def match_recipes(request: Request):
    body = await request.body()
    body_str = body.decode("utf-8")
    # print(body_str)

    parsed_data = parse_qs(body_str)
    print(parsed_data)

    matched_recipes = match_recipe(
        parsed_data["ingredients"],
        parsed_data["operator"],
        5,
        conn,
        c,
    )

    cleaned_recipes = clean_recipe(matched_recipes)
    # new_recipes = [c["name"] for c in cleaned_recipes]

    # print(new_recipes)

    # matched_recipes = crud.get_recipes_by_ingredients(db, ingredients)
    return templates.TemplateResponse(
        "index.html", {"request": request, "recipes": cleaned_recipes}
    )
