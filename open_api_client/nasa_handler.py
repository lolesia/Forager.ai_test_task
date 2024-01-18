"""Nasa endpoints parameters."""
from nasa_api_service.dto import DateDto
from open_api_client.base_handler import BaseEndpointHandler
from open_api_client.dto import RequestDTO


class BaseNasaHandler(BaseEndpointHandler):
    """Basic handler for nasa open api endpoints."""

    def __init__(self, api_key: str) -> None:
        """Initialize general parameters for making requests to nasa endpoints."""
        self.base_url = 'https://api.nasa.gov'
        self.request_params = {'api_key': api_key}


class AstronomyPictureHandler(BaseNasaHandler):
    """Handles interactions with the NASA Astronomy Picture of the Day (APOD) API."""

    def generate_request_params(self) -> RequestDTO:
        """Generate request parameters for the astronomy picture endpoint."""
        return RequestDTO(
            method='GET',
            base_url=self.base_url,
            endpoint='planetary/apod',
            request_params=self.request_params,
            headers=None,
            body=None,
        )

    def retrieve_endpoint_data(self) -> dict:
        """Retrieve information about the astronomy picture of the day from the NASA API."""
        request_dto = self.generate_request_params()
        return self.make_request(request_dto)


class InterplanetaryShockHandler(BaseNasaHandler):
    """Handles interactions with the NASA Interplanetary Shock (IPS) API."""

    def generate_request_params(self, date_dto: DateDto) -> RequestDTO:
        """Generate request parameters for the interplanetary shock endpoint."""
        return RequestDTO(
            method='GET',
            base_url=self.base_url,
            endpoint='DONKI/IPS',
            request_params=self.request_params,
            headers=None,
            body={
                'startDate': str(date_dto.start_date),
                'endDate': str(date_dto.end_date),
            },
        )

    def retrieve_endpoint_data(self, date_dto: DateDto) -> dict:
        """Retrieve information about the interplanetary shock from the NASA API."""
        request_dto = self.generate_request_params(date_dto)
        return self.make_request(request_dto)
