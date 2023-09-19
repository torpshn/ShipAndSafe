from django.shortcuts import render
from django.shortcuts import render, redirect
from django.conf import settings
from django.http import HttpResponse, HttpRequest, JsonResponse, HttpResponseRedirect
from App.Ship import Ship
from App.Weather import Weather

# Create your views here.

def index(request):
    if request.method == 'GET':
        return render(request, template_name = 'index.html')

def get_weather(imo):
    wind_force = Weather(imo)
    data = wind_force.data_picker()
    return data

def get_info(imo):
    ship = Ship(imo)
    return ship.speed, ship.course, ship.c_lat, ship.c_lon

def show(request):
    imo = request.GET.get('imo')
    speed, course, c_lat, c_lon = get_info(imo)
    forecast_weather = get_weather(imo)

    return render(request, 'index.html', {
        'imo':imo,
        'details':True,
        'speed': speed,
        'course':course,
        'lat':c_lat,
        'lon':c_lon,
        'weather':forecast_weather
        })
