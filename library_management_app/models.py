from django.urls import reverse
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class AuthorModel(models.Model):
    name = models.CharField(max_length=80,)

    class Meta:
        ordering = ('name',)

    def get_absolute_url(self):
        return reverse('author', args=[self.pk, ])

    def __str__(self):
        return self.name


class BookModel(models.Model):

    name = models.CharField(max_length=200)

    author = models.ManyToManyField(AuthorModel, related_name='books')

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


# from library_management_app.models import BookModel, AuthorModel
# from django.contrib.auth.models import User

# user = User.objects.get(username='admin')

# author1 = AuthorModel(name='Napoleon Hill')
# author1.save()

# book1 = BookModel(name='Think and Grow Rich', description='Think and Grow Rich', user=user)
# book1.save()

# book1.author.add(author1)
# book1.author.all()

# author1.authors.filter(name='The Fifth Agreement')
