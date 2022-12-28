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


class Image(models.Model):
    place = models.ForeignKey(
        'Place',
        on_delete=models.CASCADE,
        verbose_name='Место',
        related_name='images'

    )
    photo = models.ImageField(
        upload_to='media', verbose_name='Файл изображения'
    )
    sort_index = models.PositiveSmallIntegerField(
        verbose_name='Порядок вывода', default=0
    )

    def __str__(self) -> str:
        return f'{self.sort_index} {self.place.title}'

    class Meta:
        verbose_name = 'Image'
        verbose_name_plural = 'Images'
        ordering = ['sort_index']