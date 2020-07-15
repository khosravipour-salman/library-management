from django.urls import path, reverse
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.index, name='index'),

    path('register/', views.register_page, name='register'),
    path('login/', views.login_page, name='login'),
    path('logout/', views.logout_user, name='logout'),

    path('books/', views.booklist_page, name='books'),
    path('books/add_book', views.add_book, name='add_book'),
    path('books/edit_book/<int:pk>/', views.edit_book, name='edit_book'),
    path('books/delete_book/<int:pk>/', views.delete_book, name='delete_book'),
    path('books/<int:pk>/', views.single_book, name='single_book'),
    path('books/<int:pk>/share/', views.share_book, name='share_book'),
    path('books/author/<int:pk>/', views.author_page, name='author'),
    path('books/add_author/', views.add_author, name='add_author'),


    path('users/', views.userlist_page, name='users'),
    path('users/delete/<int:pk>', views.delete_user, name='delete_user'),
    path('users/promote/<int:pk>', views.promote_user, name='promote_user'),

    path('user/', views.user_page, name='user'),

    path(
        'user/reset_password',
        auth_views.PasswordResetView.as_view(
            template_name='accounts/reset_password/password_reset.html'),
        name='reset_password'
    ),

    path(
        'user/reset_password_sent',
        auth_views.PasswordResetDoneView.as_view(
            template_name='accounts/reset_password/password_reset_sent.html'),
        name='password_reset_done'
    ),
    path(
        'user/reset_password/<uidb64>/<token>',
        auth_views.PasswordResetConfirmView.as_view(
            template_name='accounts/reset_password/password_reset_form.html'),
        name='password_reset_confirm'),

    path(
        'user/reset_password_complete',
        auth_views.PasswordResetCompleteView.as_view(
            template_name='accounts/reset_password/password_reset_done.html'),
        name='password_reset_complete'),
]
