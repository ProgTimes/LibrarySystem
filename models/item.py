from dataclasses import dataclass


@dataclass
class LibraryItem:
    title: str
    author: str
    publication_year: int

    def display_info(self) -> None:
        print(f"Title: {self.title}\n"
              f"Author: {self.author}\n"
              f"Year: {self.publication_year}")
