# 2. Create a class Book with a protected attribute _book_id and a protected method
# _display_id() that prints the book ID. Then, create a subclass LibraryBook that allows the
# librarian to access and display the book ID.


class Book:
    def __init__(self, book_id):
        self._book_id = book_id

    def _display_id(self):
        print("Book ID:", self._book_id)


class LibraryBook(Book):
    def display_book_id(self):
        self._display_id()


# Example usage
book = LibraryBook("12345")
book.display_book_id()