class BookDetails:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
    def print_title(self):
        print(f"Book Title: {self.title}")
    def print_author(self):
        print(f"Author: {self.author}")
    def print_isbn(self):
        print(f"ISBN: {self.isbn}")
class InventoryManagement:
    def __init__(self, quantity, price):
        self.quantity = quantity
        self.price = price
    def print_quantity(self):
        print(f"Quantity in stock: {self.quantity}")
    def print_total_value(self):
        print(f"Total Value: ${self.calculate_total_value():.2f}")
    def calculate_total_value(self):
        return self.quantity * self.price
    def update_quantity(self, quantity):
        self.quantity = quantity

class Book:
    def __init__(self, title, author, isbn, quantity, price):
        self.book_details = BookDetails(title, author, isbn)
        self.inventory = InventoryManagement(quantity, price)

    def display_book_information(self):
        print("Book Information:")
        self.book_details.print_title()
        self.book_details.print_author()
        self.book_details.print_isbn()
        self.inventory.print_quantity()
        self.inventory.print_total_value()


# An example of creating and displaying book information using the combined single-class structure
book1 = Book("Refactoring", "Martin Fowler", "978-0201485677", 50, 47.99)
book1.display_book_information()
