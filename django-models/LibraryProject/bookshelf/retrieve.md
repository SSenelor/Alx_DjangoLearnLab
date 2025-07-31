<<<<<<< HEAD
from bookshelf.models import Book

# Retrieve the book instance
book = Book.objects.get(title="1984")
book.title    # Output: '1984'
book.author   # Output: 'George Orwell'
book.publication_year  # Output: 1949
=======
from bookshelf.models import Book

# Retrieve the book instance
book = Book.objects.get(title="1984")
book.title    # Output: '1984'
book.author   # Output: 'George Orwell'
book.publication_year  # Output: 1949
>>>>>>> f36242daa0bd743ab358d08120859cfdb2977878
