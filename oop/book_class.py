class Book:
    def __init__(self, title, author, year):
        """Constructor to initialize the book's attributes."""
        self.title = title
        self.author = author
        self.year = year

    def __del__(self):
        """Destructor to print a message when the book object is deleted."""
        print(f"Deleting {self.title}")

    def __str__(self):
        """String representation to display a user-friendly description of the book."""
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        """Official representation that recreates the Book object."""
        return f"Book('{self.title}', '{self.author}', {self.year})"

