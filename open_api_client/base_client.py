"""Base API Client."""
import requests

from open_api_client.interface import ApiClientInterface


class BaseApiClient(ApiClientInterface):
    """Base API client implementing common functionality for making HTTP requests."""

    def get_request(self, endpoint: str, request_params: dict = None, headers: dict = None, body: dict = None) -> dict:
        """Make a GET request to the specified API endpoint."""
        url = '{0}/{1}'.format(self.url, endpoint)
        response = requests.get(url, params=request_params, headers=headers, data=body, timeout=10)
        response.raise_for_status()
        return response.json()
