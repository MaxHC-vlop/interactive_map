from places.models import Place
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.urls import reverse


def show_template(request):
    places = Place.objects.all()
    features = []
    for place in places:
        features.append(
            {
                'type': 'Feature',
                'geometry': {
                    'type': 'Point',
                    'coordinates': (
                        place.longitude,
                        place.latitude,
                    )
                },
                'properties': {
                    'title': place.title,
                    'placeId': place.id,
                    'detailsUrl': reverse('places', args=[place.id])
                }
            }
        )
    feature_collection = {
        'type': 'FeatureCollection',
        'features': features
    }

    context = {'feature_collection': feature_collection}

    return render(request, 'index.html', context)


def show_places(request, place_id=1):
    place = get_object_or_404(Place, pk=place_id)
    place_context = {
        'title': place.title,
        'imgs': [
            img.photo.url
            for img in place.images.order_by('sort_index')
        ],
        'description_short': place.description_short,
        'description_long': place.description_long,
        'coordinates': {
            'lat': place.latitude,
            'lng': place.longitude
        }
    }

    return JsonResponse(
        place_context, json_dumps_params={'ensure_ascii': False}
    )
