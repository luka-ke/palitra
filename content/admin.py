from django.contrib import admin
from .models import Category, Article, Tag


class ArticleAdmin(admin.ModelAdmin):
    filter_horizontal = ('tags',)

class TagAdmin(admin.ModelAdmin):
    pass

admin.site.register(Article, ArticleAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Category)