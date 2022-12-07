from django.shortcuts import render
from .models import Book
from django.db import connection
# Create your views here.

def books_list(request):
    books = Book.objects.all()
    print(connection.queries)
    return render(
        request,
        "books/list.html",
        {"books": books}
    )

def book_details(request, id):
    book = Book.objects.get(id=id)
    return render(
        request,
        "books/details.html",
        {"book": book}
    )