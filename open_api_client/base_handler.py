"""Base endpoint handler."""
import requests

from open_api_client.dto import RequestDTO
from open_api_client.interface import EndpointHandlerInterface


class BaseEndpointHandler(EndpointHandlerInterface):
    """Base Endpoint Handler implementing common functionality for making HTTP requests."""

    def make_request(self, request_dto: RequestDTO) -> dict:
        """Make an HTTP request to the specified API endpoint."""
        request_url = '{0}/{1}'.format(request_dto.base_url, request_dto.endpoint)
        response = requests.request(
            request_dto.method,
            request_url,
            params=request_dto.request_params,
            headers=request_dto.headers,
            data=request_dto.body,
            timeout=10,
        )
        response.raise_for_status()
        return response.json()
