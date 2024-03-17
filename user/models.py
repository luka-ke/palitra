from django.db import models

class User(models.Model):
    id = models.CharField(primary_key=True, max_length=100)
    image = models.ImageField(upload_to='user/images/', blank=True, null=True)
    description = models.TextField()
    username = models.EmailField(unique=True)
    is_author = models.BooleanField(default=False)