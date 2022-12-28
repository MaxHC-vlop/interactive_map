from django.db import models


class Place(models.Model):
    title = models.CharField(
        max_length=100, verbose_name='Название'
    )
    description_short = models.TextField(
        max_length=255, verbose_name='Краткое описание', blank=True
    )
    description_long = models.TextField(
        verbose_name='Полное описание', blank=True
    )
    lng = models.FloatField(verbose_name='Широта')
    lat = models.FloatField(verbose_name='Долгота')

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = 'Place'
        verbose_name_plural = 'Places'