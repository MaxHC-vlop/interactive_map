from django.contrib import admin
from places.models import Place


@admin.register(Place)
class PlaceAdminModel(admin.ModelAdmin):
    pass