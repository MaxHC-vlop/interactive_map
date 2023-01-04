from django.contrib import admin
from places.models import Place, Image
from adminsortable2.admin import SortableInlineAdminMixin


class ImageInline(SortableInlineAdminMixin, admin.TabularInline):
    model = Image
    extra = 1
    readonly_fields = ('get_preview',)
    fields = ('photo', 'get_preview', 'sort_index',)


@admin.register(Place)
class PlaceAdminModel(admin.ModelAdmin):
    inlines = [ImageInline]
    fieldsets = [
        (None,         {'fields': ['title']}),
        ('Описание',   {'fields': ['description_short', 'description_long'], 'classes': ['collapse']}),
        ('Координаты', {'fields': ['lat', 'lng'], 'classes': ['collapse']}),
    ]