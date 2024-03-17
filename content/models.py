from django.db import models

from user.models import User


class Category(models.Model):
    id = models.CharField(primary_key=True, max_length=100)
    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='logos/', blank=True, null=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)


class Tag(models.Model):
    id = models.CharField(primary_key=True, max_length=100)
    name = models.CharField(max_length=100)


class Article(models.Model):
    id = models.CharField(primary_key=True, max_length=100)
    title = models.CharField(max_length=100)
    description = models.TextField()
    publishedAt = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='articles')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='articles')
    tags = models.ManyToManyField(Tag, blank=True)
    is_published = models.BooleanField(default=False)
    image = models.ImageField(upload_to='images/', blank=True, null=True)

