from django.contrib import admin
from places.models import Place, Image


@admin.register(Place)
class PlaceAdminModel(admin.ModelAdmin):
    pass


@admin.register(Image)
class ImageAdminModel(admin.ModelAdmin):
    pass