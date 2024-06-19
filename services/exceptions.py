class BookException(Exception):
    pass


class BookNotFound(BookException):
    def __init__(self):
        super().__init__("Book not found")


class BookAlreadyExists(BookException):
    def __init__(self):
        super().__init__("Book already exists")


class BookAlreadyBorrowed(BookException):
    def __init__(self):
        super().__init__("Book is already borrowed")


class BookNotBorrowed(BookException):
    def __init__(self):
        super().__init__("Book is not borrowed")
