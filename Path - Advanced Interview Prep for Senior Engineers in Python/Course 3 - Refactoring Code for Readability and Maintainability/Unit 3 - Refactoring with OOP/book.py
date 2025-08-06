class Book:
    def __init__(self, title, author, isbn, price):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.price = price

    def display_book_info(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"ISBN: {self.isbn}")
        print(f"Price: ${self.price:.2f}")

    def apply_discount(self, discount_percentage):
        self.price *= (1 - discount_percentage / 100)


book = Book(
    "Refactoring: Improving the Design of Existing Code",
    "Martin Fowler",
    "978-0134757599",
    47.99
)
# Display the book information
book.display_book_info()
# Apply a 10% discount to the book
book.apply_discount(10)
# Display the book information again to show the updated price
print("After applying discount:")
book.display_book_info()
