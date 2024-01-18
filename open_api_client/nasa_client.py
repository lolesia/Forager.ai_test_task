"""Nasa Open API Client."""
from open_api_client.nasa_handler import AstronomyPictureHandler, InterplanetaryShockHandler


class NasaOpenApiClient(object):
    """Nasa Open API Client."""

    def __init__(self, api_key: str) -> None:
        """Initialize NasaOpenApi object."""
        self.apod = AstronomyPictureHandler(api_key)
        self.ips = InterplanetaryShockHandler(api_key)
