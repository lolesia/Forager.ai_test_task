"""Nasa Open API Client."""
import os

from dotenv import load_dotenv

from nasa_api_service.dto import DateDto
from open_api_client.base_client import BaseApiClient
from open_api_client.nasa_endpoint_data import NasaEndpointRequestParams

load_dotenv()


class NasaOpenApiClient(BaseApiClient):
    """Nasa Open API Client."""

    def __init__(self) -> None:
        """Initialize NasaOpenApi object."""
        super().__init__()
        self.base_url = 'https://api.nasa.gov'
        self.request_params = {'api_key': os.environ.get('NASA_SECRET_KEY')}
        self.endpoint_params = NasaEndpointRequestParams(self.base_url, self.request_params)

    def astronomy_picture_of_the_day(self) -> dict:
        """
        Retrieve information about the astronomy picture of the day.

        You can find NASA API Documentation for Astronomy Picture of the Day:
        https://api.nasa.gov/ in section APOD
        """
        request_dto = self.endpoint_params.astronomy_picture_request_params()
        return self.make_request(request_dto)

    def geomagnetic_storm(self, date_dto: DateDto) -> dict:
        """
        Retrieve information about the geomagnetic storm.

        You can find NASA API Documentation for Astronomy Picture of the Day:
        https://api.nasa.gov/ in section DONKI/Geomagnetic Storm (GST)
        """
        request_dto = self.endpoint_params.geomagnetic_storm_request_params(date_dto)
        return self.make_request(request_dto)
