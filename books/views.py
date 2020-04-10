from django.shortcuts import render
from django.views import View
from .models import Book
from . import forms
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .serializers import BookSerializer

from django.http import HttpResponse


# Create your views here.
def index_view(request):
    return render(request, 'books/index.html')


def book_list(request):
    # get all books from DB
    books = Book.objects.all()
    context = {
        'books': books
    }
    return render(request, 'books/book_list.html', context=context)


def book_delete(request, book_id):
    # get book by its ID then delete it
    book = Book.objects.get(pk=book_id)
    book.delete()
    context = {
        'notification_title': 'Book deleted notification',
        'notification_content': f'The book id {book_id} has been deleted',
    }
    return render(request, 'books/notification.html', context=context)


class BookModifying(View):
    def get(self, request, book_id):
        # get book with specific id
        book = Book.objects.get(pk=book_id)
        context = {
            'book_id': book.id,
            'book_title': book.title,
            'book_content': book.content,
        }
        return render(request, 'books/book_modifying.html', context=context)

    def post(self, request, book_id):
        book = Book.objects.get(pk=book_id)
        # get POST data
        data = request.POST

        # set new book title and content
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


class BookInput(View):
    def get(self, request):
        # create form to input book data based on BookInputForm
        book_form = forms.BookInputForm()
        context = {
            'book_form': book_form,
        }
        return render(request, 'books/book_input.html', context=context)

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
                book_data.save()
            except Exception as e:
                context['notification_content'] = f'Something wrong, cannot save data. Error: {e}'
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


@api_view(['GET'])
def book_list_api(request):
    books = Book.objects.all()
    serializer = BookSerializer(books, many=True)
    return Response(data=serializer.data, status=status.HTTP_200_OK)


class BookModifyingAPI(APIView):
    def get(self, request, book_id):
        book = Book.objects.get(pk=book_id)
        serializer = BookSerializer(book)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def put(self, request, book_id):
        return HttpResponse(f'You request a PUT method on this book id: {book_id}')
