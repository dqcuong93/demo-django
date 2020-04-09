from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .models import Book
from . import forms


# Create your views here.
def index_view(request):
    return HttpResponse('YOU ARE IN THE INDEX PAGE!')


def book_list(request):
    # get all books from DB
    books = Book.objects.all()
    context = {
        'books': books
    }
    return render(request, 'books/books_list.html', context=context)


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

        book.title = data.get('book_title')
        book.content = data.get('book_content')
        book.save()

        return HttpResponse(f'Book id "{book_id}" has been modified.')


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
        # if Book data valid then save into database
        if book_data.is_valid():
            book_data.save()
            return HttpResponse('Data saved!')
        else:
            return HttpResponse('Data is not valid!')
