from .views import *
from django.urls import path, include
from google import views as view

urlpatterns = [
    path('', view.home, name="home"),
    path('geocode', view.geocode, name="geocode"),
    path('geocode/locations/<int:pk>', view.geocode_locations, name="geocode_club"),

    path('distance', view.distance, name="distance"),
    path('map/<int:id>', view.map, name="map"),
    path('mydata/<int:id>', view.mydata, name="mydata"),
    path('calculate/distance/<int:pk>/<int:pk2>', view.calculate_distance, name="calculate_distance"),
]
