# do zgodności z Python 2
# from __future__ import unicode_literals, absolute_import, print_function
# from django.utils.encoding import python_2_unicode_compatible
import uuid
from django.db import models
from django.urls import reverse
# from raport.models import raport  ( z innej aplikacji)
from django.utils.translation import ugettext_lazy as _

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


class BookCategory(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=100)
    # author = models.ForeignKey(Author, on_delete=models.CASCADE)   #przy zmianie typu pola
    # lepiej utworzyć nowe, niz zmieniać stare
    authors = models.ManyToManyField(Author)
    categories = models.ManyToManyField(BookCategory)

    # raport = models.ForeignKey("raports.Raport") jeśli FK z innej aplikacji
    # którą wcześniej trzeba zaimportować

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('shelf:book-detail', args=[str(self.id)])

class BookEdition(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="editions")
    isbn = models.CharField(max_length=17)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    date = models.DateField()

    def __str__(self):
        return f'{self.book.title} {self.publisher.name}'


COVER_TYPES = (
    ('soft', 'Soft'),  #  (wartość w bazie, wartość wyświetlana)
    ('hard', 'Hard')
)
class BookItem(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    edition = models.ForeignKey(BookEdition, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, null=True, blank=True)
    cat_number = models.CharField(max_length=30)
    cover_type = models.CharField(max_length=4, choices=COVER_TYPES)
    def __str__(self):
        return f'{self.edition} {self.get_cover_type_display()}'
