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
    name = input("Please enter your name: ").strip().title()
    email = input("Email: ").strip()
    password = input("Password: ").strip()
    account_type = input("Are you an author, student or reviewer: ").strip().casefold()
    if account_type == "author":
        author = Author(name, email, password)
        author.greet()
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

if __name__ == "__main__":
    main()