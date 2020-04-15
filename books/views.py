from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import BookSerializer
from django.shortcuts import render
from rest_framework import status
from django.http import Http404
from django.views import View
from .models import Book
from . import forms


# define a function that get a book by its ID
def get_book(book_id):
    try:
        return Book.objects.get(pk=book_id)
    except Exception as e:
        return e


# define a function that get all books
def get_all_book():
    try:
        return Book.objects.select_related().all()
    except Exception as e:
        return e


# Create your views here.
def index_view(request):
    return render(request, 'books/index.html')


# show all books in DB
def book_list(request):
    # get all books from DB by call get all books function
    books = get_all_book()
    context = {
        'books': books
    }
    return render(request, 'books/book_list.html', context=context)


# delete book based on its ID
def book_delete(request, book_id):
    # call get book function then delete it
    book = get_book(book_id=book_id)
    if book:
        context = {
            'notification_title': 'Book deleted notification',
            'notification_content': '',
        }
        try:
            book.delete()
        except Exception as e:
            context['notification_content'] = e
        else:
            context['notification_content'] = f'The book id "{book_id}" with title "{book.title}" has been deleted'
        finally:
            return render(request, 'books/notification.html', context=context)
    else:
        return Http404(book)


# modifying a book by its ID
class BookModifying(View):
    def get(self, request, book_id):
        # get book with specific id
        book = get_book(book_id=book_id)
        if book:
            context = {
                'book_id': book.id,
                'book_title': book.title,
                'book_content': book.content,
            }
            return render(request, 'books/book_modifying.html', context=context)
        else:
            return Http404(book)

    @method_decorator(login_required)
    def post(self, request, book_id):
        book = get_book(book_id=book_id)
        # get POST data
        data = request.POST

        # set new book title and content
        if book:
            book.title = data.get('book_title')
            book.content = data.get('book_content')
            context = {
                'notification_title': 'Book modified notification',
                'notification_content': '',
            }
            # save to database with error checking
            try:
                book.save()
            except Exception as e:
                context['notification_content'] = f'Something wrong happened. Cannot save data with error: {e}'
            else:
                context['notification_content'] = f'Book id "{book_id}" has been modified'
            finally:
                return render(request, 'books/notification.html', context=context)
        else:
            return Http404(book)


class BookInput(View):
    def get(self, request):
        # create form to input book data based on BookInputForm
        book_form = forms.BookInputForm()
        context = {
            'book_form': book_form,
        }
        return render(request, 'books/book_input.html', context=context)

    @method_decorator(login_required)
    def post(self, request):
        # get POST data then parse into BookInputForm object
        book_data = forms.BookInputForm(request.POST)

        # create context
        context = {
            'notification_title': 'Book modified notification',
            'notification_content': '',
        }

        # if Book data valid then save into database
        if book_data.is_valid():
            try:
                # create a custom processing before saving an object by using commit=False
                book = book_data.save(commit=False)
                # get logged in user
                book.user = request.user
                book.save()
            except Exception as e:
                context['notification_content'] = f'Something wrong, cannot save data. ' \
                                                  f'Error: {e}'
            else:
                context['notification_content'] = 'Book has been saved successfully!'
            finally:
                return render(request, 'books/notification.html', context=context)
        else:
            context['notification_content'] = 'Data is not valid!'
            return render(request, 'books/notification.html', context=context)


"""
API views begins here
"""


# method 1 to list all books and create POST, PUT, DELETE, GET API
# class BookListAPI(APIView):
#     def get(self, request):
#         books = get_all_book()
#         serializer = BookSerializer(books, many=True)
#         return Response(data=serializer.data, status=status.HTTP_200_OK)
#
#     def post(self, request):
#         data = request.data
#         serializer = BookSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(data=serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class BookModifyingAPI(APIView):
#     def get(self, request, book_id):
#         book = get_book(book_id=book_id)
#         serializer = BookSerializer(book)
#         return Response(data=serializer.data, status=status.HTTP_200_OK)
#
#     def put(self, request, book_id):
#         book = get_book(book_id=book_id)
#         serializer = BookSerializer(book, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(data=serializer.data, status=status.HTTP_200_OK)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def delete(self, request, book_id):
#         book = get_book(book_id=book_id)
#         book.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


# Method 2 based on generic views module, this way is considered most efficient and fast
class BookListAPI(ListCreateAPIView):
    queryset = get_all_book()
    serializer_class = BookSerializer


# have to update the URL from 'book_id' to 'pk'
class BookModifyingAPI(RetrieveUpdateDestroyAPIView):
    queryset = get_all_book()
    serializer_class = BookSerializer
