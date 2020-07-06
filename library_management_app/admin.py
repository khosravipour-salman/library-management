from django.contrib import admin
from .models import BookModel, Comment

# Register your models here.


@admin.register(BookModel)
class BookModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'author', 'publish', 'user')
    list_filter = ('publish', 'author', 'user')
    search_fields = ('name', 'author', 'user')
    date_hierarchy = 'publish'
    ordering = ('-publish',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'book', 'created', 'active')
    list_filter = ('active', 'created', 'updated')
    search_fields = ('name', 'email', 'body')
