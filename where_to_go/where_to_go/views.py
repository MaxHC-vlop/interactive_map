from places.models import Place
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse

def show_index(request):
    places = Place.objects.all()
    features = []
    for place in places:
        features.append(
            {
                'type': 'Feature',
                'geometry': {
                    'type': 'Point',
                    'coordinates': [
                        place.lng, place.lat
                    ]
                },
                'properties': {
                    'title': place.title,
                    'placeId': place.id,
                    'detailsUrl': 'static/places/moscow_legends.json'
                }
            }
        )
    feature_collection = {
        'type': 'FeatureCollection',
        'features': features
    }

    context = {'feature_collection': feature_collection}

    return render(request, 'index.html', context)


def places(request, place_id=1):
    place = get_object_or_404(Place, pk=place_id)
    place_context = {
            'title': place.title,
            'imgs': [img.photo.url for img in place.images.all().order_by('sort_index')],
            'description_short': place.description_short,
            'description_long': place.description_long,
            'coordinates': {
                'lat': place.lat,
                'lng': place.lng
            }
        }

    return JsonResponse(place_context, json_dumps_params={'ensure_ascii': False})