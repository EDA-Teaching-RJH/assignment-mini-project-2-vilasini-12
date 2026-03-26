import csv
import re
from csv_maker import csv_main

class Author:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password
    def greet(self):
        print(f'Welcome back, {self.name}!\nCatalog updates are waiting for you!')

class Student(Author):
    def __init__(self, name, email, password, age):
        super().__init__(name, email, password, age)
        self.age = age
    def greet(self):
        print(f'Hi {self.name}!\nTrying out new recipes are always fun!')

class Reviewer(Author):
    def __init__(self, name, email, password):
        super().__init__(name, email, password)
    def greet(self):
        print(f'Hi {self.name}! Time to check the recipe stats!')

def main():
    print(f"Welcome to Vilas's Cookbook: ")
    csv_main()
    name = input("Please enter your name: ").strip().title()
    email = input("Email: ").strip()
    email_checker(email)
    password = input("Password: ").strip()
    password_checker(password)
    account_type = input("Are you an author, student or reviewer: ").strip().casefold()
    if account_type == "author":
        author = Author(name, email, password)
        author.greet()
        options = input("Do you want to add new recipes, delete recipe or view(Add, Delete, View): ").title()
        match options:
            case "Add":
                print(add_recipes())
            case "Delete":
                print(delete_recipe())
            case "View":
                view_recipe()
            case _:
                print("Invalid option selected.")
    elif account_type == "student":
        age = input("Age: ")
        reviewer = Reviewer(name, email, password)
        reviewer.greet()
        
    elif account_type == "reviewer":
        reviewer = Reviewer(name, email, password)
        reviewer.greet()
    else:
        print("Invalid Account Type.")
        raise ValueError("Invalid Account Type")


def email_checker(user_email):
    while True:
        if re.search(r"^[a-zA-Z0-9]+@gmail.com$", user_email):
            print(user_email)
            break
        else:
            print("Incorrect email!\nType valid email")
            user_email = input("Email: ").strip()

def password_checker(password):
    while True:
        password_check = input("Enter password again: ")
        if password != password_check:
            print("Passwords don't match!")
        else:
            return password

def add_recipes():
  recipe_name = input("Recipe Name: ").strip().title()
  cook_time = input("Cooking Time: ").strip()
  serving = input("Servings: ").strip()
  difficulty = input("Difficulty(Easy, Medium or Hard): ").strip().title()
  rating = input("Rating out of 5: ").strip()
  ingredients = [i.strip().title() for i in input("Ingredients (use commas): ").split(",")]
  with open("recipe_catalog.csv", 'a', newline='') as cf:
    row_names = ['Name','Cook-time','Servings','Difficulty','Ratings','Ingredients']
    writer = csv.DictWriter(cf, fieldnames=row_names)
    writer.writerow({'Name': f'{recipe_name}', 'Cook-time':f'{cook_time}', 'Servings':f'{serving}', 'Difficulty':f'{difficulty}', 'Ratings':f'{rating}', 'Ingredients':f'{ingredients}'})
  return f"Successfully added recipe {recipe_name}!"

def view_recipe():
  with open("recipe_catalog.csv") as cf:
    reader = csv.DictReader(cf)
    for row in reader:
      print("Name: " + row['Name'] + ", Cook-time:" + row["Cook-time"] + ", Servings:" +row['Servings'] + ", Difficulty:" + row['Difficulty'] + ", Ratings:" + row['Ratings'] + ", Ingredients:" + row['Ingredients']+'\n')

def delete_recipe():
  delete_recipe_line = input("What recipe do you want to delete?: ").strip().title()
  temp_data_store = []
  with open("recipe_catalog.csv", 'r') as f:
    temp_data_store = f.readlines()
  with open("recipe_catalog.csv", 'w') as f:
    for line in temp_data_store:
      if delete_recipe_line not in line.strip("\n"):
        f.write(line)
  return f"Successfully removed {delete_recipe_line} from the Catalog"

if __name__ == "__main__":
    main()