from django.shortcuts import render
from django.views.generic import DetailView, ListView
from  .models import Author, Book

class AuthorListView(ListView):
    model = Author

class AuthorDetailView(DetailView):
    model = Author

class BookListView(ListView):
    model = Book

class BookDetailView(DetailView):
    model = Book