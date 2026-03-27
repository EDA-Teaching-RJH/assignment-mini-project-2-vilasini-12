import csv
import re
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from csv_maker import csv_main

class Author:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password
    def greet(self):
        print(f'Welcome back, {self.name}!\nCatalog updates are waiting for you!')
    def leave(self):
        print(f"Thanks for the update {self.name}! You'll be logged out of {self.email}")
        exit()

class Student(Author):
    def __init__(self, name, email, password, age):
        super().__init__(name, email, password)
        self.age = age
    def greet(self):
        print(f'Hi {self.name}!\nTrying out new recipes are always fun!')
    def leave(self):
        print(f"Have fun trying this out {self.name}! You'll be logged out of {self.email}")
        exit()

class Reviewer(Author):
    def __init__(self, name, email, password):
        super().__init__(name, email, password)
    def greet(self):
        print(f'Hi {self.name}! Time to check the recipe stats!')
    def leave(self):
        print(f"Statistics has been displayed {self.name}! You'll be logged out of {self.email}")
        exit()

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
                author.leave()
            case "Delete":
                print(delete_recipe())
                author.leave()
            case "View":
                view_recipe()
                author.leave()
            case _:
                print("Invalid option selected.")
    elif account_type == "student":
        age = input("Age: ")
        student = Student(name, email, password, age)
        student.greet()
        print("Choose a recipe from the following list: \n")
        print(view_recipe())
        recipe_display()
        student.leave()
    elif account_type == "reviewer":
        reviewer = Reviewer(name, email, password)
        reviewer.greet()
        display_stats()
        reviewer.leave()
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
    method = input("Method: \n")
    with open("recipe_catalog.csv", 'a', newline='') as cf:
        row_names = ['Name','Cook-time','Servings','Difficulty','Ratings','Ingredients']
        writer = csv.DictWriter(cf, fieldnames=row_names)
        writer.writerow({'Name': f'{recipe_name}', 'Cook-time':f'{cook_time}', 'Servings':f'{serving}', 'Difficulty':f'{difficulty}', 'Ratings':f'{rating}', 'Ingredients':f'{ingredients}'})
    with open(f"{recipe_name}.txt", "w") as f:
        f.write("Method" + method)
    return f"Successfully added recipe {recipe_name}!"

def view_recipe():
  with open("recipe_catalog.csv") as cf:
    reader = csv.DictReader(cf)
    for row in reader:
      print("Name: " + row['Name'] + ", Cook-time:" + row["Cook-time"] + ", Servings:" +row['Servings'] + ", Difficulty:" + row['Difficulty'] + ", Ratings:" + row['Ratings'] + ", Ingredients:" + row['Ingredients']+ "\n")

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

def recipe_display():
    chosen_recipe = input("What recipe do you want to give a try: ").strip().title()
    match chosen_recipe:
        case "Banana Bread":
            with open("banana_bread.txt") as rf:
                contents = rf.read()
                print(contents)
        case "Pancakes":
            with open("pancakes.txt") as rf:
                contents = rf.read()
                print(contents)
        case "Crispy Tofu":
            with open("crispy_tofu.txt") as rf:
                contents = rf.read()
                print(contents)
        case "Prawn Spaghetti":
            with open("prawn_spaghetti.txt") as rf:
                contents = rf.read()
                print(contents)
        case "Chicken Stirfry":
            with open("chicken_stirfry.txt") as rf:
                contents = rf.read()
                print(contents)
        case _:
            print("Invalid recipe chosen.")
            raise ValueError("Invalid recipe chosen")
    
def display_stats():
    names = []
    ratings = []
    cooking_time = []
    with open("recipe_catalog.csv") as cf:
        reader = csv.DictReader(cf)
        for row in reader:
            names.append(row['Name'])
            ratings.append(float(row['Ratings']))
            cooking_time.append(int(row["Cook-time"]))
    x = np.array(names)
    y = np.array(ratings)
    z = np.array(cooking_time)

    plt.title("Recipe Ratings")
    plt.xlabel("Recipes")
    plt.ylabe("Ratings (out of 5)")
    plt.bar(x,y)
    plt.show()
    plt.title("Cooking Time")
    plt.xlabel("Recipes")
    plt.ylabel("Cooking Time (mins)")
    plt.ylim(0,70)
    plt.bar(x,z)
    plt.show()
    exit()


if __name__ == "__main__":
    main()