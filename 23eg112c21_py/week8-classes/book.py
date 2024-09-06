class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def set_title(self, title):
        self.title = title

    def set_author(self, author):
        self.author = author

    def set_price(self, price):
        self.price = price

    def get_title(self):
        return self.title

    def get_author(self):
        return self.author

    def get_price(self):
        return self.price

    def display_details(self):
        print(f"Title: {self.title}, Author: {self.author}, Price: {self.price}")

# Create book instances
books = [
    Book("Book One", "Author One", 29.99),
    Book("Book Two", "Author Two", 39.99),
    Book("Book Three", "Author Three", 49.99),
    Book("Book Four", "Author Four", 59.99),
    Book("Book Five", "Author Five", 69.99)
]

# Display book details
for book in books:
    book.display_details()