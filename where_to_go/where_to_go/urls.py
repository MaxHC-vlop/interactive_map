from django.contrib import admin
from django.urls import path
from where_to_go.views import show_index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', show_index),
]