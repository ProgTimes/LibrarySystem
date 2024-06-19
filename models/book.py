import enum
from dataclasses import dataclass

from models.item import LibraryItem


class BookCondition(enum.Enum):
    BAD, NORMAL, GOOD = range(0, 3)


@dataclass
class Book(LibraryItem):
    is_borrowed: bool = False
    book_condition: BookCondition = BookCondition.NORMAL

    def display_info(self) -> None:
        super().display_info()
        print(f"Is borrowed: {self.is_borrowed}\n"
              f"Book condition: {self.book_condition.name}")
