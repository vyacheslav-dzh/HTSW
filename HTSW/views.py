from django.shortcuts import render
from django.http import HttpResponse
from .models import Routes
import json


def create_line(stops, i, color, count):
    res = ''
    stops = json.loads(stops)
    res += f'var {i} = new ymaps.Polyline(\n' \
           f'{stops}\n' \
           ',{' \
           f'balloonContent: "{count} безбилетников"' \
           '},\n' \
           '{balloonCloseButton: true,\n' \
           f'strokeColor: "{color}",\n' \
           'strokeWidth: 4,\n' \
           'strokeOpacity: 0.8});\n'
    return res


def generate_routes():
    routes = Routes.objects.all()
    res = 'ymaps.ready(init);\n' \
          'function init(){\n' \
          'var map = new ymaps.Map("map", {\n' \
          'center: [55.76, 37.64],\n' \
          'zoom: 10\n' \
          '});\n'
    ending = 'map.geoObjects'
    for i in range(len(routes)):
        line_name = f'polyline{i}'
        color = '#474A51'
        count = int(routes[i].r_count_stowaways)
        if count >= 20:
            color = '#ff0000'
        elif count >= 10:
            color = '#ffff00'
        elif count == 0:
            color = '#00ff00'
        res += create_line(routes[i].r_stops, line_name, color, count)
        ending += f'.add({line_name})'
    res += ending
    res += '}'

    return res


def home(request):

    script = generate_routes()

    return render(request, 'index.html', {'script': script})


def test(request):
    return HttpResponse('<h1>Test page</h1>')




