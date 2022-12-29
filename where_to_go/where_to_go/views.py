from places.models import Place
from django.shortcuts import render


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