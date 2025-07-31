<<<<<<< HEAD
from bookshelf.models import Book

# Update the book title
book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.save()

# Check the update
book.title  # Output: 'Nineteen Eighty-Four'
=======
from bookshelf.models import Book

# Update the book title
book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.save()

# Check the update
book.title  # Output: 'Nineteen Eighty-Four'
>>>>>>> f36242daa0bd743ab358d08120859cfdb2977878
