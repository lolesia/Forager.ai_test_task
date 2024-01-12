"""Base API Client."""
from typing import Optional

import requests

from open_api_client.interface import ApiClientInterface


class BaseApiClient(ApiClientInterface):
    """Base API client implementing common functionality for making HTTP requests."""

    def __init__(self, url: str):
        """Initialize BaseApiClient object."""
        self.url = url

    def make_request(
        self,
        method: str,
        endpoint: str,
        request_params: Optional[dict] = None,
        headers: Optional[dict] = None,
        body: Optional[dict] = None,
    ) -> dict:
        """Make an HTTP request to the specified API endpoint."""
        url = '{0}/{1}'.format(self.url, endpoint)
        response = requests.request(
            method,
            url,
            params=request_params,
            headers=headers,
            data=body,
            timeout=10,
        )
        response.raise_for_status()
        return response.json()
