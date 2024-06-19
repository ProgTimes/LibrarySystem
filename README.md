**Library Management System**

**Objective**: you need to create a simple library management system that allows users to add books, borrow books, return books, and view available books.
 
**Tasks**:
1) Create a base class LibraryItem with attributes title, author, publication_year.
2) Create a subclass Book that inherits from LibraryItem with attributes is_borrowed and book_condition (you can make it a string or use Enum - https://realpython.com/python-enum/).
3) Implement a method display_info() in the LibraryItem class that prints out the details of the item. Override this method in the Book class to include book-specific details.
4) Create a Library class that contains a collection of LibraryItem objects.  This class should provide methods to add items, remove items, borrow items (changing specified Book is_borrowed attribute to True), return items (the opposite of a previous argument) and display available non-borrowed items.
5) Implement error handling for cases such as attempting to borrow a book that is not available or returning a book that was not borrowed.
