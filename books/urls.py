from rest_framework.urlpatterns import format_suffix_patterns
from django.urls import path
from . import views
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.views.decorators.cache import cache_page
from django.conf import settings

CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)

app_name = 'books'
urlpatterns = [
    path('', views.index_view, name='index'),
    path('books/', views.book_list, name='book_list'),
    path('books/book-input', views.BookInput.as_view(), name='book_input'),
    path('books/<int:book_id>', views.BookModifying.as_view(), name='book_modifying'),
    path('books/book-delete/<int:book_id>', views.book_delete, name='book_delete'),
    path('books/search', views.book_search, name='book_search_result'),

    # API begins here
    # path('api/books/', views.BookListAPI.as_view(), name='book_list_api'),

    # cache_page(CACHE_TTL)
    path('api/books/', cache_page(CACHE_TTL)(views.BookListAPI.as_view()), name='book_list_api'),

    # path('api/books/<int:book_id>', views.BookModifyingAPI.as_view(), name='book_modifying_api'),
    # update to use generic views, change 'book_id' to 'pk'
    path('api/books/<int:pk>', views.BookModifyingAPI.as_view(), name='book_modifying_api'),
]
