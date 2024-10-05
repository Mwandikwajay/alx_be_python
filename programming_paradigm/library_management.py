class Book:
    def __init__(self, title, author):
        """Initialize the book with title, author, and checked-out status."""
        self.title = title
        self.author = author
        self._is_checked_out = False  # Private attribute to track availability

    def check_out(self):
        """Mark the book as checked out."""
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False

    def return_book(self):
        """Mark the book as returned."""
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False

    def is_available(self):
        """Check if the book is available."""
        return not self._is_checked_out


class Library:
    def __init__(self):
        """Initialize the library with an empty collection of books."""
        self._books = []

    def add_book(self, book):
        """Add a book to the library collection."""
        self._books.append(book)

    def check_out_book(self, title):
        """Check out a book from the library by its title."""
        for book in self._books:
            if book.title == title and book.is_available():
                book.check_out()
                print(f"You have checked out '{title}'.")
                return
        print(f"'{title}' is either not available or already checked out.")

    def return_book(self, title):
        """Return a book to the library by its title."""
        for book in self._books:
            if book.title == title and not book.is_available():
                book.return_book()
                print(f"You have returned '{title}'.")
                return
        print(f"'{title}' is not checked out or does not belong to this library.")

    def list_available_books(self):
        """List all available books in the library."""
        available_books = [book for book in self._books if book.is_available()]
        if available_books:
            for book in available_books:
                print(f"{book.title} by {book.author}")
        else:
            print("No books are currently available.")

