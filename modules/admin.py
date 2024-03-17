from django.contrib import admin

from .models import Menu, Block


class BlockAdmin(admin.ModelAdmin):
    filter_horizontal = ('articles',)
admin.site.register(Menu)
admin.site.register(Block, BlockAdmin)


