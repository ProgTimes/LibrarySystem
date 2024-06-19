from services import exceptions
from models.book import Book


class Library:
    def __init__(self):
        self._library = []

    def _get_object_by_title(self, title: str) -> Book:
        for obj in self._library:
            if obj.title == title:
                return obj
        raise exceptions.BookNotFound

    def add_book(self, book: Book) -> None:
        try:
            self._get_object_by_title(book.title)
        except exceptions.BookNotFound:
            self._library.append(book)
        else:
            raise exceptions.BookAlreadyExists

    def remove_book(self, title: str) -> None:
        book = self._get_object_by_title(title)
        self._library.remove(book)

    def borrow_book(self, title: str) -> None:
        book = self._get_object_by_title(title)
        if book.is_borrowed:
            raise exceptions.BookAlreadyBorrowed
        book.is_borrowed = True

    def return_book(self, title: str) -> None:
        book = self._get_object_by_title(title)
        if not book.is_borrowed:
            raise exceptions.BookNotBorrowed
        book.is_borrowed = False

    def available_books(self) -> list:
        return [book for book in self._library if not book.is_borrowed]

    def print_available_books(self) -> None:
        for book in self.available_books():
            book.display_info()
            print()
