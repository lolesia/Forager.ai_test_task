"""Interface for Open Api Client."""
from abc import ABC, abstractmethod

from open_api_client.dto import RequestDTO


class ApiClientInterface(ABC):
    """Abstract base class for API clients."""

    @abstractmethod
    def make_request(self, request_dto: RequestDTO) -> dict:
        """Abstract method for making POST requests."""
        # Abstract method; to be implemented in subclasses.
        ...
