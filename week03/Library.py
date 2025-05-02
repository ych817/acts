# library_manager.py

class Book:
    """
    Represents a single book with title, author, and publication year.
    """
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        """
        Returns a string representation of the book.
        """
        return f'"{self.title}" by {self.author} ({self.year})'


class Library:
    """
    Represents a library that contains a list of books.
    """
    def __init__(self):
        self.books = []

    def add_book(self, book):
        """
        Adds a Book object to the library.
        """
        self.books.append(book)

    def __str__(self):
        """
        Returns a string showing all books in the library.
        """
        if not self.books:
            return "The library has no books."
        lines = ["Books in the library:"]
        for book in self.books:
            lines.append(str(book))
        return "\n".join(lines)


# ----- Example usage -----
if __name__ == "__main__":
    # Create some Book instances
    book1 = Book("To Kill a Mockingbird", "Harper Lee", 1960)
    book2 = Book("1984", "George Orwell", 1949)
    book3 = Book("The Great Gatsby", "F. Scott Fitzgerald", 1925)

    # Create a Library and add books
    my_library = Library()
    my_library.add_book(book1)
    my_library.add_book(book2)
    my_library.add_book(book3)

    # Print the contents of the library
    print(my_library)
