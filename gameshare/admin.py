from django.contrib import admin
from django.utils.html import format_html
from .models import BoardGame

class BoardGameAdmin(admin.ModelAdmin):
    list_display = ('name', 'owner', 'genre', 'created_at', 'image_preview')

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="width: 50px; height:auto;" />'.format(obj.image.url))
        return ""
    image_preview.short_description = 'Image Preview'

admin.site.register(BoardGame, BoardGameAdmin)
