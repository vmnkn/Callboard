from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user}'


class Post(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    title = models.CharField(max_length=128, unique=True)
    text = models.TextField()
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    time_create = models.DateField(auto_now_add=True)
    time_update = models.DateField(auto_now=True)

    category = models.ManyToManyField('Category', through='PostToCategory')

    def __str__(self):
        return f'{self.title}, {self.text}'

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])


class Category(models.Model):
    name = models.CharField(max_length=64, unique=True)
    subscribers = models.ManyToManyField(User, related_name='categories')

    def __str__(self):
        return f'{self.name}'


class Comment(models.Model):
    user = models.ForeignKey(Author, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    text = models.CharField(max_length=1024)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.text}'


class PostToCategory(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
