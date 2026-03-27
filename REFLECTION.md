# Developer Journal - Vilas's Cookbook

## Project Overview
A recipe cookbook system with role-based access for authors, students and reviewers. Contains CSV/TXT file handling, OOP, regex validation, data visualisation and testing.

## Regular Expressions(REGEX)
- Used `re.search()` in `email_checker()` to validate email formats. System only accepts `@gmail.com` or `@kent.ac.uk` with the use of OR logic in `(gmail.com|kent.ac.uk)` and characters`[a-zA-Z0-9]`
- Used regex `(?=.*[A-Z])(?=.*\d).{6,}$` in `password_checker()` to validate password strength — must have at least 6 characters, one uppercase letter and one digit
- This connects to the parts in workshop 8 for domain validation. The workshop information helped to define sets and the use of OR operator helped filter different domains of interest. Applied the skills learnt to create a password strength validator that is later used to match.

## Testing
- Used `pytest` to test class (`Author`, `Student`, `Reviewer`) to verify that the attributes are stored correctly through inheritance
- Tested `recipe_display()` with `pytest.raises(ValueError)` to make sure invalid recipe name inputs are handled
- Tested `email_checker()` with valid and invalid email formats
- This connects to the workshop 8 for writing unit tests, handling exceptions and string testing. Used the workshop as a base to test invalid and valid emails but expanded on this through the use of try-except to handle Assertion errors with printed message and matching assertions to expected output. With some research, also found ways to test Error raises for invalid inputs.

## Libraries
- `csv` — reading, writing and appending recipe catalog data
- `re` — email and password strength validation
- `matplotlib` — bar charts for recipe ratings and cooking time
- `pandas` — reading CSV into DataFrames and converting data types for plotting for bar charts. Also converts recipe dict into DataFrame for CSV
- `pytest` — testing recipe_cookbook.py to make sure functions are working correctly
- Created custom library `csv_maker` which uses `pandas` and `seaborn` to initialise the recipe catalog CSV
- This connects to workshop 7 about Library usage. The workshop helped with the use of `matplotlib` for plotting the bar charts and labelling axis. The skills from workshop also helped a little with the use of `pytest`. Researched on other libraries like `csv`,`pandas` and `seaborn` to make handling of data easier and efficient

## File I/O
- CSV: read (`view_recipe`, `display_stats`), append (`add_recipes`), rewrite/read&write(`delete_recipe`)
- TXT: write recipe methods (`add_recipes`), read recipe methods (`recipe_display`)
- Used `csv.DictReader` and `csv.DictWriter` for structured CSV handling
- Expanded on the skills learnt from workshop 7 to rewrite (read and write) CSV file to delete certain data no matter the location. Handles CSV and TXT files at the same time with appropriate use. Decided CSV is best for holding dicts on recipe details and method is best to be kept in text files. Prevents too much data being placed together.

## Object-Oriented Programming
- `Author` base class stores shared attributes (`name`, `email`, `password`) and methods (`greet`, `leave`)
- `Student` inherits from `Author`, adds `age`, and modifies `greet` and `leave` to have student specific messages
- `Reviewer` inherits from `Author` and modifies `greet` and `leave` to have reviewer specific messages
- Used `super().__init__()` to reuse the parent constructor
- Demonstrates Hierarchical inheritance(`Student` and `Reviewer` are child classes to the Parent class `Author`), polymorphism(Unique messages in greet and leave methods) and encapsulation(user data stored in class)
- Used workshop 9 as a base to create inheritance in classes (with Student having an additional attribute).

## Above and Beyond
- List comprehension for adding ingredients from user into recipe catalog in the same format
- `pandas` DataFrame for data handling in `display_stats()` 
- `pandas` and `seaborn` to create own library to make CSV file
- `try/except` for handling file errors in testing
- Tested Errors raised `with pytest.raises(ValueError):`
- Password strength validation using minimum characters limitation alongside password double checker
- Login system that validates both email and password, checks password match and stores user data to selected role class.
- Role-based access control with different functionality
- Data visualisation with labelled axes and custom y-axis limits
- Using `pandas` to convert columns into numeric for order in y-axis plots
- Deleting certain recipe data from CSV file - no matter the location of recipe in file - and preserving other existing recipes.

## Challenges and Solutions
- **Deleting certain data on CSV without losing data**: Used read mode (`r`) to store data temporarily in a list and then wrote (`w`) back into the CSV file by going through temporary list and only adding data that does not match user’s delete_recipe_line
- **Cook time sorting on charts**: Resolved by converting string values to numeric using `pd.to_numeric()` by `pandas` and adding y-axis range limit `plt.ylim(0,70)`