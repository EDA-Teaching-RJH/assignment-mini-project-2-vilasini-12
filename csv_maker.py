import pandas as pd
import seaborn as sns

recipe_catalog = [
  {'Name':'Banana Bread', 'Cook-time':'50', 'Servings':'10', 'Difficulty':'Easy', 'Ratings': '4.6', 'Ingredients':['Flour', 'Bicarbonate Soda', 'Salt', 'Butter', 'Sugar', 'Eggs', 'Bananas', 'Buttermilk', 'Vanilla Extract']},
  {'Name':'Pancakes', 'Cook-time':'10', 'Servings':'6', 'Difficulty':'Easy', 'Ratings': '4.5',  'Ingredients':['Flour', 'Salt', 'Eggs', 'Milk', 'Butter']},
  {'Name':'Crispy Tofu', 'Cook-time':'15', 'Servings':'4', 'Difficulty':'Medium', 'Ratings': '3.9',  'Ingredients':['Tofu', 'Soy Sauce', 'Oil', 'Garlic', 'Ginger', 'Paprika', 'Salt', 'Cornflour']},
  {'Name':'Prawn Spaghetti', 'Cook-time':'25', 'Servings':'2', 'Difficulty':'Hard', 'Ratings': '4.3',  'Ingredients':['Spaghetti', 'Broccoli', 'Cherry Tomatoes', 'Prawns', 'Oil', 'Chilli Flakes', 'Black Pepper']},
  {'Name':'Chicken Stirfry', 'Cook-time':'8', 'Servings':'1', 'Difficulty':'Hard', 'Ratings': '5',  'Ingredients':['Oil', 'Garlic', 'Chicken Thighs', 'Red Pepper', 'Soy Sauce', 'Green Beans', 'Chicken Stock', 'Noodles']}
]

def csv_main():
  df = pd.DataFrame(recipe_catalog)
  df.to_csv('recipe_catalog.csv', index = False)

if __name__ == "__csv_main__":
  csv_main()