class BookException(Exception):
    message: str

    def __str__(self):
        return self.message


class BookNotFound(BookException):
    message = "Book not found"


class BookAlreadyExists(BookException):
    message = "Book already exists"


class BookAlreadyBorrowed(BookException):
    message = "Book is already borrowed"


class BookNotBorrowed(BookException):
    message = "Book is not borrowed"
