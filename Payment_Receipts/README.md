# Recipe PDF Generator

A Python script that creates a PDF document with a table of recipes using ReportLab.

## Installation

Install the required library:

```
pip install reportlab
```

## Usage

Run the script:

```
python recipe_generator.py
```

This will create a `recipes.pdf` file in the same directory.

## What it does

The script generates a PDF with:
- Title: "Recipe Collection"
- Table with columns: Recipe Name, Category, Prep Time, Servings, Difficulty
- Sample recipes included (Chicken Biryani, Chocolate Cake, etc.)

## Customizing recipes

Edit the `DATA` list in the code:

```python
DATA = [
    ["Recipe Name", "Category", "Prep Time", "Servings", "Difficulty"],
    ["Your Recipe", "Main Course", "30 mins", "4", "Easy"],
    # Add more recipes here
]
```

## Difficulty levels

- Easy: Simple recipes for beginners
- Medium: Intermediate cooking skills needed
- Hard: Advanced techniques required

## Requirements

- Python 3.x
- ReportLab library
