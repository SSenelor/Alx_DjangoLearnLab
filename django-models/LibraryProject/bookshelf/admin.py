<<<<<<< HEAD
from django.contrib import admin
from .models import Book

# Register your models here.

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')  # Columns shown in list view
    list_filter = ('publication_year', 'author')            # Sidebar filter options
    search_fields = ('title', 'author')                     # Search bar for title and author
=======
from django.contrib import admin
from .models import Book

# Register your models here.

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')  # Columns shown in list view
    list_filter = ('publication_year', 'author')            # Sidebar filter options
    search_fields = ('title', 'author')                     # Search bar for title and author
>>>>>>> f36242daa0bd743ab358d08120859cfdb2977878
