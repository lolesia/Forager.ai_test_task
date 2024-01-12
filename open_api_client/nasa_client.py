"""Nasa Open API Client."""
import os

from dotenv import load_dotenv

from nasa_api_service.dto import DateDto
from open_api_client.base_client import BaseApiClient

load_dotenv()


class NasaOpenApiClient(BaseApiClient):
    """Nasa Open API Client."""

    def __init__(self) -> None:
        """Initialize NasaOpenApi object."""
        self.url = 'https://api.nasa.gov'
        self.request_parameters = {'api_key': os.environ.get('NASA_SECRET_KEY')}


class AstronomyPictureApiClient(NasaOpenApiClient):
    """API client for the astronomy picture endpoint."""

    def astronomy_picture_of_the_day(self) -> dict:
        """
        Retrieve information about the astronomy picture of the day.

        You can find NASA API Documentation for Astronomy Picture of the Day:
        https://api.nasa.gov/ in section APOD
        """
        endpoint = 'planetary/apod'
        method = 'GET'
        return self.make_request(method, endpoint, self.request_parameters)


class GeomagneticStormApiClient(NasaOpenApiClient):
    """API client for the geomagnetic storm endpoint."""

    def geomagnetic_storm(self, date_dto: DateDto) -> dict:
        """
        Retrieve information about the geomagnetic storm.

        You can find NASA API Documentation for Astronomy Picture of the Day:
        https://api.nasa.gov/ in section DONKI/Geomagnetic Storm (GST)
        """
        endpoint = 'DONKI/GST'
        method = 'GET'
        self.request_parameters.update({
            'startDate': str(date_dto.start_date),
            'endDate': str(date_dto.end_date),
        })
        return self.make_request(method, endpoint, self.request_parameters)
