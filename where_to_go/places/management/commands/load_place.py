from urllib.parse import urlparse
from io import BytesIO

import requests

from django.core.files.base import ContentFile
from django.core.management.base import BaseCommand
from places.models import Place, Image


class Command(BaseCommand):
    help = 'Getting data from json.'

    def add_arguments(self, parser):
        parser.add_argument(
            'url',
            nargs='+',
            type=str,
            help='Json file url'
        )

    def upload_images(self, images, place):
        for number, image in enumerate(images, start=1):
            try:
                filename = urlparse(image).path.split('/')[-1]
                response = requests.get(image)
                response.raise_for_status()

                image = BytesIO(response.content)
                photo = ContentFile(image.read(), name=filename)
                Image.objects.create(
                    sort_index=number,
                    place=place,
                    photo=photo
                )

                self.stdout.write(f'Load {place.title}')

            except requests.exceptions.HTTPError as error:
                self.stdout.write(f'Error load: {image}\n{error}')
                continue

            except requests.exceptions.ConnectionError as error:
                self.stdout.write(f'Error load: {image}\n{error}')
                continue

    def handle(self, *args, **options):
        self.stdout.write(f'Load data...{len(options["url"])}')
        for url in options["url"]:
            try:
                response = requests.get(url)
                response.raise_for_status()
                place_content = response.json()

            except requests.exceptions.HTTPError as error:
                self.stdout.write(f'Error load: {error}')
                continue

            except requests.exceptions.ConnectionError as error:
                self.stdout.write(f'Error load: {error}')
                continue

            try:
                place, created = Place.objects.update_or_create(
                    title=place_content['title'],
                    defaults={
                        'description_short': place_content.get(
                            'description_short', ''
                        ),
                        'description_long': place_content.get(
                            'description_long', ''
                        ),
                        'latitude': place_content['coordinates']['lat'],
                        'longitude': place_content['coordinates']['lng']
                    }
                )
                self.stdout.write(f'Load {place.title} {created}')

            except KeyError as error:
                self.stdout.write(f'Error load: {error}')
                continue

            except Place.MultipleObjectsReturned as error:
                self.stdout.write(f'Error load: {error}')
                continue

            if created:
                images = place_content.get('imgs', [])
                self.upload_images(images, place)
