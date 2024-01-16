"""Nasa Open API Client."""
from dotenv import load_dotenv

from nasa_api_service.dto import DateDto
from open_api_client.nasa_handler import BaseNasaHandler

load_dotenv()


class NasaOpenApiClient(object):
    """Nasa Open API Client."""

    def __init__(self, endpoint_handler: BaseNasaHandler) -> None:
        """Initialize NasaOpenApi object."""
        self.endpoint_handler = endpoint_handler

    def astronomy_picture_of_the_day(self) -> dict:
        """
        Retrieve information about the astronomy picture of the day.

        You can find NASA API Documentation for Astronomy Picture of the Day:
        https://api.nasa.gov/ in section APOD
        """
        return self.endpoint_handler.astronomy_picture_of_the_day()

    def geomagnetic_storm(self, date_dto: DateDto) -> dict:
        """
        Retrieve information about the geomagnetic storm.

        You can find NASA API Documentation for Astronomy Picture of the Day:
        https://api.nasa.gov/ in section DONKI/Geomagnetic Storm (GST)
        """
        return self.endpoint_handler.geomagnetic_storm(date_dto)
