'''
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views
from .views import list_books, LibraryDetailView, user_login, user_logout, register

urlpatterns = [
    path('books/', list_books, name='list_books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
]

 # Authentication URLs
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('register/', register, name='register'),

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('relationship_app.urls')),  # Include app-level URLs
]


from django.urls import path
from .views import (
    list_books, LibraryDetailView, user_login, user_logout, register,
    admin_view, librarian_view, member_view
)

urlpatterns = [
    # existing routes
    path('books/', list_books, name='list_books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('register/', register, name='register'),

    # new role-based routes
    path('admin-role/', admin_view, name='admin_view'),
    path('librarian-role/', librarian_view, name='librarian_view'),
    path('member-role/', member_view, name='member_view'),
]


from .views import add_book, edit_book, delete_book

urlpatterns += [
    path('books/add/', add_book, name='add_book'),
    path('books/edit/<int:pk>/', edit_book, name='edit_book'),
    path('books/delete/<int:pk>/', delete_book, name='delete_book'),
]
from django.urls import path
from . import views

urlpatterns = [
    path("books/", views.list_books, name="list_books"),
]
'''

from django.urls import path
from django.contrib.auth import views as auth_views # Import Django's built-in auth views
from .views import (
    list_books,
    LibraryDetailView,
    user_login,  # If you have a custom user_login view, keep it
    user_logout, # If you have a custom user_logout view, keep it
    register,    # Your custom registration view
    admin_view,
    librarian_view,
    member_view,
    add_book,
    edit_book,
    delete_book,
)

urlpatterns = [
    # Book Management URLs
    path('books/', list_books, name='list_books'),
    path('books/add/', add_book, name='add_book'),
    path('books/edit/<int:pk>/', edit_book, name='edit_book'),
    path('books/delete/<int:pk>/', delete_book, name='delete_book'),

    # Library Detail URL
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),

    # Custom Authentication URLs (if you prefer your own views for more control)
    # If you have custom user_login and user_logout views, use these:
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('register/', register, name='register'), # Your custom register view

    # OR, use Django's built-in authentication views (more common for login/logout)
    # Uncomment and use these if you want to leverage Django's default login/logout views.
    # Make sure to create 'registration/login.html' and 'registration/logged_out.html' templates.
    # path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    # path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
    # Note: For LogoutView, 'next_page' redirects after logout. You might want a 'logged_out.html' template too.
    # path('logout/', auth_views.LogoutView.as_view(template_name='registration/logged_out.html'), name='logout'),


    # Role-Based URLs
    path('admin-role/', admin_view, name='admin_view'),
    path('librarian-role/', librarian_view, name='librarian_view'),
    path('member-role/', member_view, name='member_view'),
]
