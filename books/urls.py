from rest_framework.urlpatterns import format_suffix_patterns
from django.urls import path

from . import views

app_name = 'books'
urlpatterns = [
    path('', views.index_view, name='index'),
    path('books/', views.book_list, name='book_list'),
    path('books/<int:book_id>', views.BookModifying.as_view(), name='book_modifying'),
    path('books/book-input', views.BookInput.as_view(), name='book_input'),
    path('books/book-delete/<int:book_id>', views.book_delete, name='book_delete'),

    # API begins here
    # path('api/books/', views.book_list_api, name='book_list_api'),
    path('api/books/', views.BookListAPI.as_view(), name='book_list_api'),
    # path('api/books/<int:book_id>', views.BookModifyingAPI.as_view(), name='book_modifying_api'),
    # update to use generic views
    path('api/books/<int:pk>', views.BookModifyingAPI.as_view(), name='book_modifying_api'),
]
