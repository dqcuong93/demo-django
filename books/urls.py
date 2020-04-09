from django.urls import path
from . import views

app_name = 'books'
urlpatterns = [
    path('', views.index_view, name='index'),
    path('books/', views.book_list, name='book_list'),
    path('books/<int:book_id>', views.BookModifying.as_view(), name='book_modifying'),
    path('books/book-input', views.BookInput.as_view(), name='book_input'),
]
