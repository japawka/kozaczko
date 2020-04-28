from django.shortcuts import render, HttpResponse
from django.views.generic import DetailView, ListView, TemplateView
from  .models import Author, Book
# from django.views import View

# class MainPageView(TemplateView):
#     def get(self, request, *args, **kwargs):
#         return render(HttpResponse('OK'))

# index_view = MainPageView.as_view()

class MainPageView(TemplateView):
    template_name = 'index.html'

class AuthorListView(ListView):
    model = Author

class AuthorDetailView(DetailView):
    model = Author

class BookListView(ListView):
    model = Book

class BookDetailView(DetailView):
    model = Book