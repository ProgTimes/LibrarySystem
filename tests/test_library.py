import pytest

from models.library_item import Book
from services import exceptions
from services.library import Library


@pytest.fixture(scope='function')
def library():
    return Library()


@pytest.fixture(scope='function')
def book():
    return Book(title="The Lord of the Rings", author="J. R. R. Tolkien", publication_year=1954)


@pytest.fixture(scope='function')
def borrowed_book():
    return Book(title="The Lord of the Rings", author="J. R. R. Tolkien", publication_year=1954, is_borrowed=True)


def test_add_book(library: Library, book: Book):
    library.add_book(book)
    assert library.available_books()[0].title == book.title
    assert library.available_books()[0].author == book.author
    assert library.available_books()[0].publication_year == book.publication_year
    assert library.available_books()[0].is_borrowed == book.is_borrowed
    assert library.available_books()[0].book_condition == book.book_condition


def test_add_same_books(library: Library, book: Book):
    library.add_book(book)
    with pytest.raises(exceptions.BookAlreadyExists):
        library.add_book(book)


def test_remove_book(library: Library, book: Book):
    library.add_book(book)
    assert len(library.available_books()) == 1
    library.remove_book(book.title)
    assert len(library.available_books()) == 0


def test_remove_book_not_exist(library: Library, book: Book):
    with pytest.raises(exceptions.BookNotFound):
        library.remove_book(book.title)


def test_borrow_book(library: Library, book: Book):
    library.add_book(book)
    library.borrow_book(book.title)
    assert len(library.available_books()) == 0


def test_borrow_book_not_exist(library: Library, book: Book):
    with pytest.raises(exceptions.BookNotFound):
        library.borrow_book(book.title)


def test_borrow_book_borrowed(library: Library, borrowed_book: Book):
    library.add_book(borrowed_book)
    with pytest.raises(exceptions.BookAlreadyBorrowed):
        library.borrow_book(borrowed_book.title)


def test_return_book(library: Library, borrowed_book: Book):
    library.add_book(borrowed_book)
    library.return_book(borrowed_book.title)
    assert len(library.available_books()) == 1


def test_return_book_not_exist(library: Library, book: Book):
    with pytest.raises(exceptions.BookNotFound):
        library.return_book(book.title)


def test_return_book_not_borrowed(library: Library, book: Book):
    library.add_book(book)
    with pytest.raises(exceptions.BookNotBorrowed):
        library.return_book(book.title)
