"""Serializers for NASA Open API."""
from rest_framework import serializers


class ApodDTOSerializer(serializers.Serializer):
    """Serializer for astronomy picture of the day data."""

    date = serializers.DateField()
    explanation = serializers.CharField()
    name = serializers.CharField()
    image_link = serializers.URLField()


class IPSDTOSerializer(serializers.Serializer):
    """Serializer for interplanetary shock data."""

    id = serializers.IntegerField()
    activity_id = serializers.CharField()
    location = serializers.URLField()
    link = serializers.CharField()


class DateSerializer(serializers.Serializer):
    """Serializer for date data."""

    start_date = serializers.DateField()
    end_date = serializers.DateField()
