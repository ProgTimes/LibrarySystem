import enum
from dataclasses import dataclass


class BookCondition(enum.Enum):
    BAD, NORMAL, GOOD = range(0, 3)


@dataclass
class LibraryItem:
    title: str
    author: str
    publication_year: int

    def display_info(self) -> None:
        print(
            f"Title: {self.title}\n"
            f"Author: {self.author}\n"
            f"Year: {self.publication_year}"
        )


@dataclass
class Book(LibraryItem):
    is_borrowed: bool = False
    book_condition: BookCondition = BookCondition.NORMAL

    def display_info(self) -> None:
        super().display_info()
        print(
            f"Is borrowed: {self.is_borrowed}\n"
            f"Book condition: {self.book_condition.name}"
        )
