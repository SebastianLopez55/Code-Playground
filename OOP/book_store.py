"""

UML Diagram
-------------
|   Book    |
|-----------|
| - title: str
| - author: str
| - isbn: str
|-----------|
| + __str__(): str
-------------


-------------
|  Library  |
|-----------|
| - books: dict<isbn, Book>
| - rented_books: dict<isbn, Book>
|-----------|
| + add_book(book: Book): bool
| + remove_book(isbn: str): bool
| + rent_book(isbn: str): bool
| + return_book(isbn: str): bool
| + list_books(): list<str>
| + list_rented_books(): list<str>

"""


class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn

    def __str__(self):
        return f"{self.title} by {self.author} (ISBN: {self.isbn})"


class Library:
    def __init__(self):
        self.books = {}
        self.rented_books = {}

    def add_book(self, book):
        if book.isbn not in self.books:
            self.books[book.isbn] = book
            return True
        return False

    def remove_book(self, isbn):
        if isbn in self.books:
            if isbn in self.rented_books:
                del self.rented_books[isbn]
            del self.books[isbn]
            return True
        return False

    def rent_book(self, isbn):
        if isbn in self.books and isbn not in self.rented_books:
            self.rented_books[isbn] = self.books[isbn]
            return True
        return False

    def return_book(self, isbn):
        if isbn in self.rented_books:
            del self.rented_books[isbn]
            return True
        return False

    def list_books(self):
        return [str(book) for book in self.books.values()]

    def list_rented_books(self):
        return [str(book) for book in self.rented_books.values()]


# Example usage:
library = Library()

# Adding books to the library
book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", "1234567890")
book2 = Book("1984", "George Orwell", "1234567891")
library.add_book(book1)
library.add_book(book2)

# Listing books
print("Books in library:")
for book in library.list_books():
    print(book)

# Renting a book
library.rent_book("1234567890")

# Listing books after renting one
print("\nBooks in library after renting 'The Great Gatsby':")
for book in library.list_books():
    print(book)

print("\nRented books:")
for book in library.list_rented_books():
    print(book)

# Returning a book
library.return_book("1234567890")

# Listing books after returning one
print("\nBooks in library after returning 'The Great Gatsby':")
for book in library.list_books():
    print(book)

print("\nRented books:")
for book in library.list_rented_books():
    print(book)
