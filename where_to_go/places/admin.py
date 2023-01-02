from django.contrib import admin
from places.models import Place, Image


class ImageInline(admin.TabularInline):
    model = Image


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