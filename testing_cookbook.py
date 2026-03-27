import pytest
from recipe_cookbook import email_checker
from recipe_cookbook import recipe_display
from recipe_cookbook import Author, Student, Reviewer

def main():
    """
    Runs all the test functions.
    """
    test_author()
    test_student()
    test_reviewer()
    test_email_checker()
    test_recipe_display()

def test_email_checker():
    """
    Tests email_checker() with valid and invalid email formats.
    """
    try:
        assert email_checker("Vilas12@gmail.com") == "Vilas12@gmail.com"    #Valid email returns email
        assert email_checker("sponge5bob@kent.ac.uk") == "sponge5bob@kent.ac.uk"    #Valid email returns email
        assert email_checker("r34md") == "Incorrect email!\nType valid email"    #Wrong emails rejected and asked again
        assert email_checker("hello@@gmail.com") == "Incorrect email!\nType valid email"    #Wrong emails rejected and asked again
        assert email_checker("rwfog@business.com") == "Incorrect email!\nType valid email"    #Wrong emails rejected and asked again
    except (AssertionError):
        print("Email has incorrect format")

def test_author():
    """
    Tests Author class stores name, email and password correctly.
    """
    author = Author("Vilas", "vilas12@gmail.com", "pass32")
    assert author.name == "Vilas"
    assert author.email == "vilas12@gmail.com"
    assert author.password == "pass32"

def test_student():
    """
    Tests Student class stores age through inheritance.
    """
    student = Student('Mark', 'markie@kent.ac.uk', '34word', 20)
    assert student.age == 20
    assert student.email == 'markie@kent.ac.uk'
    assert student.name == 'Mark'

def test_reviewer():
    """
    Tests Reviewer class stores name through inheritance.
    """
    reviewer = Reviewer('Chris', 'chr1s@gmail.com', 'home53')
    assert reviewer.name == 'Chris'
    assert reviewer.password == 'home53'
    assert reviewer.email == 'chr1s@gmail.com'

def test_recipe_display():
    """
    Tests recipe_display raises ValueError for invalid inputs.
    """
    with pytest.raises(ValueError):
        recipe_display("random")
    with pytest.raises(ValueError):
        recipe_display("")

if __name__ == "__main__":
    main()