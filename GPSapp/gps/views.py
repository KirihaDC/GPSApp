from django.shortcuts import render
from django.http import JsonResponse
import geocoder

def gps_view(request):
    g = geocoder.ip('me')
    latitude, longitude = g.latlng

    return render(request, 'gps/gps_view.html', {
        'latitude': latitude,
        'longitude': longitude,
    })

def get_gps_data(request):
    g = geocoder.ip('me')
    return JsonResponse({'lat': g.latlng[0], 'lng': g.latlng[1]})
