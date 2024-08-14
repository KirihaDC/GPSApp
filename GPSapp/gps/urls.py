from django.urls import path
from .views import gps_view, get_gps_data
from . import views

urlpatterns = [
    path('', gps_view, name='gps_view'),
    path('gps-data/', get_gps_data, name='get_gps_data'),
]
