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