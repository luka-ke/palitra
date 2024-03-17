from django.db import models

from content.models import Category, Article
from adminsortable.models import SortableMixin
from enum import Enum

class BlockType(Enum):
    STANDARD = 'standard'
    VERTICAL = 'vertical'
    HORIZONTAL = 'horizontal'

class Menu(SortableMixin):
    order = models.PositiveIntegerField(default=0)  # Numeric field for ordering
    name = models.CharField(max_length=100, default='default_value')
    link = models.CharField(max_length=100)
    is_external = models.BooleanField(default=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='menus')
    is_active = models.BooleanField(default=False)
    class Meta(SortableMixin.Meta):
        ordering = ['order']  # Ordering by the 'order' field

class Block(models.Model):
    id = models.CharField(primary_key=True, max_length=100)
    articles = models.ManyToManyField(Article, blank=True)
    vizualType = models.CharField(max_length=20, choices=[(tag.value, tag.name) for tag in BlockType])
    position = models.IntegerField(default=0)
    title = models.CharField(max_length=250)
    display_title = models.BooleanField(default=True)

