from django.contrib import admin
from places.models import Place, Image
from django.utils.html import format_html


class ImageInline(admin.TabularInline):
    model = Image

    readonly_fields = ('get_preview',)
    fields = ('photo', 'get_preview', 'sort_index',)

    def get_preview(self, obj, width=200):
        return format_html(
            f'<img src="{obj.photo.url}" width="{width}" />'
        )


@admin.register(Place)
class PlaceAdminModel(admin.ModelAdmin):
    fieldsets = [
        (None,         {'fields': ['title']}),
        ('Описание',   {'fields': ['description_short', 'description_long'], 'classes': ['collapse']}),
        ('Координаты', {'fields': ['lat', 'lng'], 'classes': ['collapse']}),
    ]
    inlines = [ImageInline]


@admin.register(Image)
class ImageAdminModel(admin.ModelAdmin):
    pass