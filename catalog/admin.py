from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from catalog.models import LiteraryFormat, Book, Author

admin.site.register(LiteraryFormat)
admin.site.register(Book)
admin.site.register(Author, UserAdmin)
