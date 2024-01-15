"""Nasa endpoints parameters."""
from nasa_api_service.dto import DateDto
from open_api_client.dto import RequestDTO


class NasaEndpointRequestParams(object):
    """Generates request parameters for NASA endpoints."""

    def __init__(self, base_url: str, request_params: dict) -> None:
        """Initialize a NasaEndpointRequestParams object."""
        self.base_url = base_url
        self.request_params = request_params

    def astronomy_picture_request_params(self) -> RequestDTO:
        """Generate request parameters for the astronomy picture endpoint."""
        return RequestDTO(
            method='GET',
            base_url=self.base_url,
            endpoint='planetary/apod',
            request_params=self.request_params,
            headers=None,
            body=None,
        )

    def geomagnetic_storm_request_params(self, date_dto: DateDto) -> RequestDTO:
        """Generate request parameters for the geomagnetic storm endpoint."""
        return RequestDTO(
            method='GET',
            base_url=self.base_url,
            endpoint='DONKI/GST',
            request_params=self.request_params,
            headers=None,
            body={
                'startDate': str(date_dto.start_date),
                'endDate': str(date_dto.end_date),
            },
        )
