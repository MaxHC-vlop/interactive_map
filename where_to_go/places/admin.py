from django.contrib import admin
from places.models import Place, Image
from adminsortable2.admin import SortableInlineAdminMixin
from django.utils.html import format_html


class ImageInline(SortableInlineAdminMixin, admin.TabularInline):
    model = Image
    extra = 1
    readonly_fields = ('get_preview',)
    fields = ('photo', 'get_preview', 'sort_index',)

    def get_preview(self, obj, height=200):
        return format_html(
            '<img src="{}" height="{}" />',
            obj.photo.url,
            height
        )
    get_preview.short_description = 'ИЗОБРАЖЕНИЕ'


@admin.register(Place)
class PlaceAdminModel(admin.ModelAdmin):
    inlines = [ImageInline]
    fieldsets = [
        (None, {
            'fields': ['title']
        }),
        ('Описание', {
            'fields': ['description_short', 'description_long'],
            'classes': ['collapse']
        }),
        ('Координаты', {
            'fields': ['latitude', 'longitude'],
            'classes': ['collapse']
        }),
    ]
