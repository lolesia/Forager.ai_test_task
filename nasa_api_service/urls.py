"""URL patterns for the NASA API application."""
from django.urls import path

from nasa_api_service.views import AstronomyPictureNASAView, InterplanetaryShockNASAView, InterplanetaryShockNASADetailView

urlpatterns = [
    path('picture_of_the_day/', AstronomyPictureNASAView.as_view()),
    path('interplanetary_shock/', InterplanetaryShockNASAView.as_view()),
    path('interplanetary_shock/<int:pk>/', InterplanetaryShockNASADetailView.as_view()),
]
