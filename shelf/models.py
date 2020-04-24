from django.db import models
from django.urls import reverse
# from raport.models import raport  ( z innej aplikacji)

class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    def get_absolute_url(self):
        return reverse('shelf:author-detail', args=[str(self.id)])

class Publisher(models.Model):
    name = models.CharField(max_length=80)

    def __str__(self):
        return self.name
    # def get_absolute_url(self):
    #     return reverse('publisher-detail', args=[str(self.id)])

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    isbn = models.CharField(max_length=17)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    # raport = models.ForeignKey("raports.Raport") jeśli FK z innej aplikacji
    # którą wcześniej trzeba zaimportować

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('shelf:book-detail', args=[str(self.id)])