# Boolean Recipe Matcher

Boolean Recipe Matcher is a FastAPI application that allows users to search for recipes based on ingredients and boolean operators (AND/OR) between them. The application provides a user-friendly interface to input ingredients and view matched recipes with detailed instructions.

## Features

- Add multiple ingredients with AND/OR boolean operators.
- View matched recipes with detailed instructions.
- Responsive and interactive UI with tooltips for recipe details.

## Project Structure
```
.
├── app
│   ├── main.py
│   ├── static
│   │   ├── css
│   │   │   └── styles.css
│   │   └── js
│   │       └── scripts.js
│   └── templates
│       ├── base.html
│       └── index.html
├── data
│   ├── recipes.db
│   └── recipes.json
├── __init__.py
├── license.txt
├── readme.md
├── requirements.txt
├── run.sh
├── str
└── utils
    ├── boolean_match.py
    ├── build_recipe.py
    ├── __init__.py
    └── utils.py
```

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/skfrost19/Boolean-Recipe-Match.git
    cd Boolean-Recipe-Match
    ```

2. Create a virtual environment and activate it:
    ```sh
    python3 -m venv venv
    source venv/bin/activate
    ```

3. Install the dependencies:
    ```sh
    pip install -r requirements.txt
    ```

## Running the Application

1. Start the FastAPI server:
    ```sh
    ./run.sh
    ```

2. Open your browser and go to `http://127.0.0.1:8000`.

## Usage

1. Enter ingredients in the input fields.
2. Select AND/OR boolean operators between ingredients.
3. Click "Match Recipes" to view matched recipes.
4. Click the info button (i) next to each recipe to view detailed instructions in a tooltip.
5. Close the tooltip by clicking the close button (×) or clicking outside the tooltip.

## Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -am 'Add new feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Create a new Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](license.txt) file for details.