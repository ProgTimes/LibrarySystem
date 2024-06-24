from models.library_item import Book
from services.library import Library

if __name__ == '__main__':
    library = Library()
    book1 = Book(title="The Lord of the Rings", author="J. R. R. Tolkien", publication_year=1954)
    library.add_book(book1)
    book2 = Book(title="Python Concurrency with Asyncio", author="Matthew Fowler", publication_year=2022)
    library.add_book(book2)

    library.print_available_books()

    print("===================================", end="\n\n")

    library.borrow_book("Python Concurrency with Asyncio")

    library.print_available_books()
