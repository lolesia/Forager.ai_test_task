"""URL configuration for core project."""
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('nasa/', include('nasa_api.urls')),
]
