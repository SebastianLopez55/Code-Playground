"""
Book
    > pages: List[str]

    write()

Library
    > book_collection : {id : [Book(), rented bool]}
    > rented_book bool
    > book_count int

    add_books()
    rent_books()
    is_rented()


"""


class Book:
    def __init__(self, page_count, book_title) -> None:
        self.book_title = book_title
        self.page_count = page_count
        self.pages = (page_count + 1) * [" "]

    def write(self, page, content):
        self.pages[page] = content
        print(f'Just wrote "{content}" to book. ')


class Library:
    def __init__(self) -> None:
        self.book_collection = dict()
        self.book_count = 0

    def add_book(self, book, book_id):
        if book_id not in self.book_collection:
            self.book_collection[book_id] = [book, False]
            self.book_count += 1
            print(f'Book "{book.book_title}" added to library.')

    def is_rented(self, book_id):
        if book_id not in self.book_collection:
            print(f"Book with id {book_id} not in collection.")

        return self.book_collection[book_id][1]

    def rent_book(self, book_id):
        if not self.is_rented(book_id):
            book_info = self.book_collection[book_id]
            book_info[1] = True
            return book_info[0]

    def book_catalog(self):
        print("Book Catalog: ")
        for book_id, book_info in self.book_collection.items():
            print(
                f'Book with id "{book_id}" and title "{book_info[0].book_title}" is available: {not self.is_rented(book_id)}'
            )


# Book 1
def book_factory(title, pages, content):
    book = Book(pages, title)
    for i in range(1, pages + 1):
        book.write(i, content)
    return book


book1 = book_factory("Harry Potter Summary", 5, "bla bla bla bla")
book2 = book_factory("Bed Stories", 4, "Sleep story ...")

lib = Library()
lib.add_book(book1, "A43")
lib.add_book(book2, "A76")

print(lib.is_rented("A43"))
print(lib.is_rented("A76"))

lib.book_catalog()

result = lib.rent_book("A43")
if result:
    print(result.book_title)

print(lib.is_rented("A43"))
lib.book_catalog()
