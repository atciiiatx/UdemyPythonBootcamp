"""Special methods."""


class Book():
    """Book class."""

    def __init__(self, title, author, pages):
        """Constructor."""
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        """Convert to string."""
        return 'Book: ' + self.title + " Author:" + \
            self.author + " Pages:" + str(self.pages)

    def __len__(self):
        """Length."""
        return self.pages

    def __del__(self):
        """Destructor."""
        print(f'Book {self.title} is deleted.')


my_book = Book('Python Book', 'Jose', 245)
print(my_book)
print(f'book length = {len(my_book)}')
del my_book
