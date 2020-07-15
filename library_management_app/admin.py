from django.contrib import admin
from .models import BookModel, Comment, AuthorModel

# Register your models here.


@admin.register(BookModel)
class BookModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'publish', 'user')
    list_filter = ('publish', 'author', 'user')
    search_fields = ('name', 'description')
    date_hierarchy = 'publish'
    ordering = ('-publish',)
    readonly_fields = ('created',)
    autocomplete_fields = ('user',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'book', 'created', 'active')
    list_filter = ('active', 'created', 'updated')
    search_fields = ('name', 'email', 'body')
    ordering = ('created',)
    readonly_fields = ('created',)

@admin.register(AuthorModel)
class AuthorModelAdmin(admin.ModelAdmin):
        list_display = ('name',)

