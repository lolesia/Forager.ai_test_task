"""URL patterns for the NASA API application."""
from django.urls import path

from nasa_api_service.views import AstronomyPictureNASAView, GeomagneticStormNASADetailView, GeomagneticStormNASAView

urlpatterns = [
    path('picture_of_the_day/', AstronomyPictureNASAView.as_view()),
    path('geomagnetic_storm/', GeomagneticStormNASAView.as_view()),
    path('geomagnetic_storm/<int:pk>/', GeomagneticStormNASADetailView.as_view()),
]
