from django.contrib import admin
from .models import BookModel, Comment, AuthorModel, History
from search_admin_autocomplete.admin import SearchAutoCompleteAdmin
from import_export.admin import ExportMixin


@admin.register(BookModel)
class BookModelAdmin(SearchAutoCompleteAdmin):
    list_display = ('name', 'publish', 'user')
    list_filter = ('publish', 'user')
    search_fields = ('name',)
    date_hierarchy = 'publish'
    ordering = ('-publish',)
    readonly_fields = ('created',)


@admin.register(Comment)
class CommentAdmin(SearchAutoCompleteAdmin):
    list_display = ('name', 'email', 'book', 'created', 'active')
    list_filter = ('active', 'created', 'updated')
    search_fields = ('name', 'email', 'body')
    ordering = ('created',)
    readonly_fields = ('created',)


@admin.register(AuthorModel)
class AuthorModelAdmin(SearchAutoCompleteAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(History)
class HistoryAdmin(ExportMixin, SearchAutoCompleteAdmin):
    list_display = ('user', 'request_method', 'url', 'viewed')
    search_fields = ('user', 'request_method', 'viewed')
    list_filter = ('user', 'viewed')
    readonly_fields = ('user', 'request_method', 'url', 'viewed', 'request', 'user_agent')
    ordering = ('-viewed',)
