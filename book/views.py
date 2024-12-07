from django.shortcuts import render
from django.http import Http404
from .models import Category, Book

# Create your views here.

def home(request):
    categories = Category.objects.all()
    books = Book.objects.all()
    return render(request, 'index.html', {'categories': categories, 'books': books})

def category_books(request, category_id):
    try:
        category = Category.objects.get(id=category_id)
        books = category.books.all()
    except Category.DoesNotExist:
        raise Http404("Category not found")
    return render(request, 'category.html', {'category': category, 'books': books})

def book_detail(request, book_id):
    try:
        book = Book.objects.get(id=book_id)
    except Book.DoesNotExist:
        raise Http404("Book not found")
    return render(request, 'book.html', {'book': book})
