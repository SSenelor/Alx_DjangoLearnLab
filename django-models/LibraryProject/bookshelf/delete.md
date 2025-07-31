<<<<<<< HEAD
from bookshelf.models import Book

# Delete the book
book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()

# Confirm deletion
Book.objects.all()  # Output: <QuerySet []>
=======
from bookshelf.models import Book

# Delete the book
book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()

# Confirm deletion
Book.objects.all()  # Output: <QuerySet []>
>>>>>>> f36242daa0bd743ab358d08120859cfdb2977878
