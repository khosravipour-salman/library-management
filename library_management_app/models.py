from django.urls import reverse
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class BookModel(models.Model):

    name = models.CharField(max_length=200)

    author = models.CharField(max_length=200)

    description = models.TextField(default='No explanation provided')

    publish = models.DateTimeField(default=timezone.now)

    created = models.DateTimeField(auto_now_add=True)

    updated = models.DateTimeField(auto_now=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        ordering = ('-publish',)

    def get_absolute_url(self):
        return reverse('single_book', args=[self.pk, ])

    def __str__(self):
        return self.name


class Comment(models.Model):
    book = models.ForeignKey(BookModel, on_delete=models.CASCADE,
                             related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return f'Comment by {self.name} on {self.book}'
