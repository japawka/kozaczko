from . import views
from django.urls import path
app_name = 'shelf'
urlpatterns = [
    path('authors/', views.AuthorListView.as_view(), name='authors'),
    path('books/', views.BookListView.as_view(), name='books'),
    path('books/<int:pk>', views.BookDetailView.as_view(), name='book-detail'),
    path('authors/<int:pk>', views.AuthorDetailView.as_view(), name='author-detail'),
]
