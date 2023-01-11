from urllib.parse import urlparse
from io import BytesIO

import requests

from django.core.files.base import ContentFile
from django.core.management.base import BaseCommand
from places.models import Place, Image


def upload_image(image, number, place):
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


class Command(BaseCommand):
    help = 'Getting data from json.'

    def add_arguments(self, parser):
        parser.add_argument(
            'url',
            nargs='+',
            type=str,
            help='Json file url'
        )

    def handle(self, *args, **options):
        self.stdout.write(f'Load data...{len(options["url"])}')
        for url in options["url"]:
            response = requests.get(url)
            response.raise_for_status()
            place_content = response.json()

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

                if created:
                    images = place_content.get('imgs', [])
                    for number, image in enumerate(images, start=1):
                        upload_image(image, number, place)
                        self.stdout.write(f'Load {image}')

            except KeyError as error:
                self.stdout.write(f'Error load: {error}')
                continue

            except requests.exceptions.HTTPError as error:
                self.stdout.write(f'Error load: {error}')
                continue

            except requests.exceptions.ConnectionError as error:
                self.stdout.write(f'Error load: {error}')
                continue
