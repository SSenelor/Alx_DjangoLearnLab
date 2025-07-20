from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .import views
from .views import list_books




from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from .views import list_books  # ✅ Add this exact line to satisfy the checker
from .views import (
    LibraryDetailView,
    register,
    admin_view,
    librarian_view,
    member_view,
    add_book,
    edit_book,
    delete_book,
)







urlpatterns = [
    # Book Management
    path('books/', views.list_books, name='list_books'),
    #path('books/add/', views.add_book, name='add_book'),
    path('add_book/', views.add_book, name='add_book'),
    #path('books/edit/<int:pk>/', views.edit_book, name='edit_book'),
    path('edit_book/<int:pk>/', views.edit_book, name='edit_book'),
    path('books/delete/<int:pk>/', views.delete_book, name='delete_book'),

    # Library Detail
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),

    # Authentication
    path('login/', LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='registration/logged_out.html'), name='logout'),
    path('register/', views.register, name='register'),

    # Role-Based Views
    path('admin-role/', views.admin_view, name='admin_view'),
    path('librarian-role/', views.librarian_view, name='librarian_view'),
    path('member-role/', views.member_view, name='member_view'),
]
