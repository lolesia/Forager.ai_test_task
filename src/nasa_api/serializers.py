"""Serializers for NASA Open API."""
from rest_framework import serializers


class ApodDTOSerializer(serializers.Serializer):
    """Serializer for astronomy picture of the day data."""

    date = serializers.DateField()
    explanation = serializers.CharField()
    name = serializers.CharField()
    image_link = serializers.URLField()


class GstDTOSerializer(serializers.Serializer):
    """Serializer for geomagnetic storm data."""

    id = serializers.IntegerField()
    gst_id = serializers.CharField()
    link = serializers.URLField()
    kp_index = serializers.CharField()


class DateSerializer(serializers.Serializer):
    """Serializer for date data."""

    start_date = serializers.DateField()
    end_date = serializers.DateField()
