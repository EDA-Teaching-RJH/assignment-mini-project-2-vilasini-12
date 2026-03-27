import re
import csv
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from csv_maker import csv_main

class Author:
    """
    Base class for all users - including the Author itself.
    Can add, delete and view recipes.
    """
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
    """
    Inherits from Author and includes age.
    Can view recipes and methods to cook.
    """
    def __init__(self, name, email, password, age):
        super().__init__(name, email, password)
        self.age = age
    def greet(self):
        print(f'Hi {self.name}!\nTrying out new recipes are always fun!')
    def leave(self):
        print(f"Have fun trying this out {self.name}! You'll be logged out of {self.email}")
        exit()

class Reviewer(Author):
    """
    Inherits from Author.
    Can view recipe statistics - ratings and time.
    """
    def __init__(self, name, email, password):
        super().__init__(name, email, password)
    def greet(self):
        print(f'Hi {self.name}! Time to check the recipe stats!')
    def leave(self):
        print(f"All Statistics have been displayed {self.name}! You'll be logged out of {self.email}")
        exit()

def main():
    """
    This function handles user login and 
    carries out corresponding actions to account type.
    """
    print(f"Welcome to Vilas's Cookbook: ")
    csv_main()      #Initialises CSV file
    name = input("Please enter your name: ").strip().title()
    email = input("Email: ").strip()
    email_checker(email)    #Validates email's format
    password = input("Password: ").strip()
    password_checker(password)      #Confirms Password match
    account_type = input("Are you an author, student or reviewer: ").strip().casefold()
    if account_type == "author":
        author = Author(name, email, password)
        author.greet()
        #Author can add, delete or view recipes
        options = input("Do you want to add new recipes, delete recipe or view(Add, Delete, View): ").title()
        match options:
            case "Add":
                print(add_recipes())
                author.leave()  #exits after action completed
            case "Delete":
                print(delete_recipe())
                author.leave()  #exits after action completed
            case "View":
                view_recipe()
                author.leave()  #exits after action completed
            case _:
                print("Invalid option selected.")
    elif account_type == "student":
        age = input("Age: ")
        student = Student(name, email, password, age)
        student.greet()
        #Student can view recipes and choose one method to display.
        print("Choose a recipe from the following list: \n")
        print(view_recipe())
        chosen_recipe = input("What recipe do you want to give a try: ").strip().title()
        print(recipe_display(chosen_recipe))
        student.leave()  #exits after action completed
    elif account_type == "reviewer":
        reviewer = Reviewer(name, email, password)
        reviewer.greet()
        #Reviewer can see rating and cooking time stats
        display_stats()
        reviewer.leave()     #exits after action completed 
    else:
        print("Invalid Account Type.")
        raise ValueError("Invalid Account Type")


def email_checker(user_email):
    """
    This function handles the email given and checks input validation.
    Only accepts emails with @gmail.com or kent.ac.uk.
    Asks user to re-enter until email in acceptable format.

    Parameters:
    email_checker(user_email): User email

    Returns:
    user_email (str): Email saved and stored in corresponding class
    """
    while True:
        if re.search(r"^[a-zA-Z0-9]+@+(gmail.com|kent.ac.uk)$", user_email):
            print("Verified: " + user_email)
            break
        else:
            print("Incorrect email!\nType valid email")
            user_email = input("Email: ").strip()

def password_checker(password):
    """
    This function takes the password given and sees the match of 2 inputs.
    Asks user to re-enter until password matches.
    Validates password is at least 3 characters, 1 uppercase and 1 digit.

    Parameters:
    password_checker(password): Password the user sets

    Returns:
    password (str): Password saved and stored in corresponding class
    """
    while not re.search(r"^(?=.*[A-Z])(?=.*\d).{6,}$", password):
        print("Password must be at least 6 characters with one uppercase letter and one number")
        password = input("Password: ").strip()
    while True:
        password_check = input("Enter password again: ")
        if password != password_check:
            print("Passwords don't match!")
        else:
            return password


def add_recipes():
    """
    This function collects recipe details from author 
    and appends to CSV - recipe_catalog.csv -
    and saves method to text file.
    """
    recipe_name = input("Recipe Name: ").strip().title()
    cook_time = input("Cooking Time(mins): ").strip()
    serving = input("Servings: ").strip()
    difficulty = input("Difficulty(Easy, Medium or Hard): ").strip().title()
    rating = input("Rating out of 5: ").strip()
    #Splits input separated by comma into list
    ingredients = [i.strip().title() for i in input("Ingredients (use commas): ").split(",")]
    method = input("Method: \n")
    #Appends recipe to CSV file
    with open("recipe_catalog.csv", 'a', newline='') as cf:
        row_names = ['Name','Cook-time(mins)','Servings','Difficulty','Ratings','Ingredients']
        writer = csv.DictWriter(cf, fieldnames=row_names)
        writer.writerow({'Name': f'{recipe_name}', 'Cook-time(mins)':f'{cook_time}', 'Servings':f'{serving}', 'Difficulty':f'{difficulty}', 'Ratings':f'{rating}', 'Ingredients':f'{ingredients}'})
    #Writes method to a separate, new text file after recipe saved in catalog
    with open(f"{recipe_name}.txt", "w") as f:
        f.write("Method" + method)
    return f"Successfully added recipe {recipe_name}!"

def view_recipe():
  """
  This function reads CSV file 
  and displays all recipes and its details.
  """
  with open("recipe_catalog.csv") as cf:
    reader = csv.DictReader(cf)
    for row in reader:
      print("Name: " + row['Name'] + ", Cook-time(mins):" + row["Cook-time(mins)"] + ", Servings:" +row['Servings'] + ", Difficulty:" + row['Difficulty'] + ", Ratings:" + row['Ratings'] + ", Ingredients:" + row['Ingredients']+ "\n")

def delete_recipe():
  """
  This function removes a recipe from the CSV file 
  by rewriting file without the line that matches recipe name.
  """
  delete_recipe_line = input("What recipe do you want to delete?: ").strip().title()
  temp_data_store = []
  #Reads all lines to hold in a temporary list
  with open("recipe_catalog.csv", 'r') as f:
    temp_data_store = f.readlines()
  #Rewrites file excluding line matching recipe to delete
  with open("recipe_catalog.csv", 'w') as f:
    for line in temp_data_store:
      if delete_recipe_line not in line.strip("\n"):
        f.write(line)
  return f"Successfully removed {delete_recipe_line} from the Catalog"

def recipe_display(recipe):
    """
    This function displays the method for chosen recipe from its text file.

    Parameters:
    recipe_display(recipe): Choose among recipes available in CSV

    Returns:
    recipe()
    """
    match recipe:
        case "Banana Bread":
            with open("banana_bread.txt") as rf:
                contents = rf.read()
                return contents
        case "Pancakes":
            with open("pancakes.txt") as rf:
                contents = rf.read()
                return contents
        case "Crispy Tofu":
            with open("crispy_tofu.txt") as rf:
                contents = rf.read()
                return contents
        case "Prawn Spaghetti":
            with open("prawn_spaghetti.txt") as rf:
                contents = rf.read()
                return contents
        case "Chicken Stirfry":
            with open("chicken_stirfry.txt") as rf:
                contents = rf.read()
                return contents
        case _:
            raise ValueError("Invalid recipe chosen")
    
def display_stats():
    """
    This function reads recipe data from CSV using pandas
    and displays 2 bar charts: Ratings and Cooking time.
    """
    #reads CSV into a pandas DataFrame
    df = pd.read_csv("recipe_catalog.csv")
    df['Cook-time(mins)'] = pd.to_numeric(df['Cook-time(mins)'])    #converting into numeric for plotting
    df['Ratings'] = pd.to_numeric(df['Ratings'])    #converting into numeric for plotting
    #Ratings Bar Chart
    plt.title("Recipe Ratings")
    plt.xlabel("Recipes")
    plt.ylabel("Ratings (out of 5)")
    plt.bar(df['Name'], df['Ratings'])
    plt.show()
    #Cooking Time Bar Chart 
    plt.title("Cooking Time")
    plt.xlabel("Recipes")
    plt.ylabel("Cooking Time (mins)")
    plt.ylim(0, 70)
    plt.bar(df['Name'], df['Cook-time(mins)'])
    plt.show()


if __name__ == "__main__":
    main()