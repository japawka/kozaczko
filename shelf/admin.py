from django.contrib import admin
from .models import Book, Author, Publisher, BookItem, BookCategory, BookEdition

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    #list_display = ["title"]
    search_fields = ("title",)
    ordering = ['title']

# admin.site.register(Book, BookAdmin)   # teraz to z @, to jest ze starej wersji Django, ale działa
admin.site.register([Author, Publisher, BookItem, BookCategory, BookEdition])
