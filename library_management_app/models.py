from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.


class BookModel(models.Model):

    name = models.CharField(max_length=200)

    author = models.CharField(max_length=200)

    publish = models.DateTimeField(default=timezone.now)

    created = models.DateTimeField(auto_now_add=True)

    updated = models.DateTimeField(auto_now=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.name

# Remember To Add Cover Later
