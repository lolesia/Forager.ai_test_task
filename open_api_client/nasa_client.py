"""Nasa Open API Client."""
import os

from dotenv import load_dotenv

from nasa_api_service.dto import DateDto
from open_api_client.base_client import BaseApiClient

load_dotenv()


class NasaOpenApi(BaseApiClient):
    """Nasa Open API Client."""

    def __init__(self):
        """Initialize NasaOpenApi object."""
        self.api_key = os.environ.get('NASA_SECRET_KEY')
        self.url = 'https://api.nasa.gov'

    def astronomy_picture_of_the_day(self):
        """Retrieve information about the astronomy picture of the day."""
        endpoint = 'planetary/apod'
        request_parameters = {'api_key': self.api_key}
        return self.get_request(endpoint, request_parameters)

    def geomagnetic_storm(self, date_dto: DateDto) -> dict:
        """Retrieve information about the geomagnetic storm."""
        endpoint = 'DONKI/GST'
        request_parameters = {
            'api_key': self.api_key,
            'startDate': date_dto.start_date,
            'endDate': date_dto.end_date,
        }
        return self.get_request(endpoint, request_parameters)
