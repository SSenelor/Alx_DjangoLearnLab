# relationship_app/query_samples.py
'''
import os
import django

# Setup Django environment (run this if executing standalone)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_models.settings')
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

# Query all books by a specific author
author = Author.objects.get(name="Chinua Achebe")
books_by_author = Book.objects.filter(author=author)
print(f"Books by {author.name}: {[book.title for book in books_by_author]}")

# List all books in a library
library = Library.objects.get(name="Accra Central Library")
books_in_library = library.books.all()
print(f"Books in {library.name}: {[book.title for book in books_in_library]}")

# Retrieve the librarian for a library
librarian = library.librarian
print(f"Librarian of {library.name}: {librarian.name}")
'''


import os
import django

# Setup Django environment if running outside of Django shell
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

# 1. Query all books by a specific author
author_name = "Chinua Achebe"
try:
    author = Author.objects.get(name=author_name)
    books_by_author = Book.objects.filter(author=author)
    print(f"\nBooks by {author.name}:")
    for book in books_by_author:
        print(f"- {book.title}")
except Author.DoesNotExist:
    print(f"Author '{author_name}' not found.")

# 2. List all books in a library
library_name = "Accra Central Library"
try:
    library = Library.objects.get(name=library_name)
    books_in_library = library.books.all()
    print(f"\nBooks in {library.name}:")
    for book in books_in_library:
        print(f"- {book.title} by {book.author.name}")
except Library.DoesNotExist:
    print(f"Library '{library_name}' not found.")
    library = None

# 3. Retrieve the librarian for a library
if library:
    try:
        librarian = Librarian.objects.get(library=library)
        print(f"\nLibrarian of {library.name}: {librarian.name}")
    except Librarian.DoesNotExist:
        print(f"No librarian assigned to {library.name}.")
