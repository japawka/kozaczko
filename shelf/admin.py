from django.contrib import admin
from .models import Book, Author, Publisher

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ["title", "author", "publisher"]
    search_fields = ("title",)
    ordering = ['title']

# admin.site.register(Book, BookAdmin)   # teraz to z @, to jest ze starej wersji Django, ale działa
admin.site.register([Author, Publisher])
