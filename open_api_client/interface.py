"""Interface for Open Api Client."""
from abc import ABC, abstractmethod


class ApiClientInterface(ABC):
    """Abstract base class for API clients."""

    @abstractmethod
    def get_request(self, url: str, request_params: dict = None, headers: dict = None, body: dict = None) -> dict:
        """Abstract method for making POST requests."""
        # Abstract method; to be implemented in subclasses.
        ...
