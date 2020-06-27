from django.contrib import admin
from .models import BookModel

# Register your models here.


@admin.register(BookModel)
class BookModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'author', 'publish', 'user')
    list_filter = ('publish', 'author', 'user')
    search_fields = ('name', 'author', 'user')
    date_hierarchy = 'publish'
    ordering = ('-publish',)
