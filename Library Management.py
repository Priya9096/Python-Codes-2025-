# Define custom exception classes
class BookNotAvailableError(Exception):
    pass

class BookNotRentedError(Exception):
    pass

# Define the Library class
class Library:
    def __init__(self):
        self.books = {
            "Harry Potter": True,
            "The Hobbit": True,
            "1984": True,
            "The Great Gatsby": True
        }  # Dictionary to store books and their availability

    def rent_book(self, title):
        if title not in self.books or not self.books[title]:
            raise BookNotAvailableError(f"Book {title} is not available for rent.")
        self.books[title] = False
        print(f"{title} rented successfully.")

    def return_book(self, title):
        if title not in self.books or self.books[title]:
            raise BookNotRentedError(f"Book {title} was not rented.")
        self.books[title] = True
        print(f"{title} returned successfully.")

# Create an instance of Library
library = Library()

# Get user input for renting and returning books
try:
    book_to_rent = input().split(': ')[-1]
    library.rent_book(book_to_rent)
except BookNotAvailableError as e:
    print(f"Rental failed. {e}")

try:
    book_to_return = input().split(': ')[-1]
    library.return_book(book_to_return)
except BookNotRentedError as e:
    print(f"Return failed. {e}")