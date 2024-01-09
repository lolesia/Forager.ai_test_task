"""Nasa Open API Client."""

import os

import requests
from dotenv import load_dotenv
from rest_framework.status import HTTP_200_OK

from nasa_api.dto import DateDto

load_dotenv()


class NasaOpenApi(object):
    """Nasa Open API Client."""

    apod_url = 'https://api.nasa.gov/planetary/apod'  # Astronomy Picture of the Day
    gst_url = 'https://api.nasa.gov/DONKI/GST'  # Geomagnetic Storm
    nasa_api_key = os.environ.get('NASA_SECRET_KEY')

    def astronomy_picture_of_the_day(self) -> dict:
        """Retrieve information about the astronomy picture of the day."""
        request_parameters = {
            'api_key': self.nasa_api_key,
        }

        apod_info = requests.get(self.apod_url, params=request_parameters, timeout=10)
        if apod_info.status_code == HTTP_200_OK:
            return apod_info.json()
        raise RuntimeError('Not today, bro')

    def geomagnetic_storm(self, date_dto: DateDto) -> dict:
        """Retrieve information about the geomagnetic storm."""
        request_parameters = {
            'api_key': self.nasa_api_key,
            'startDate': date_dto.start_date,
            'endDate': date_dto.end_date,
        }

        gst_info = requests.get(self.gst_url, params=request_parameters, timeout=10)
        if gst_info.status_code == HTTP_200_OK:
            return gst_info.json()
        raise RuntimeError('Not today, bro')
