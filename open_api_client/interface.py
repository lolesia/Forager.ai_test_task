"""Interface for Open Api Client."""
from abc import ABC, abstractmethod
from typing import Optional


class ApiClientInterface(ABC):
    """Abstract base class for API clients."""

    @abstractmethod
    def make_request(
        self,
        method: str,
        endpoint: str,
        request_params: Optional[dict] = None,
        headers: Optional[dict] = None,
        body: Optional[dict] = None,
    ) -> dict:
        """Abstract method for making POST requests."""
        # Abstract method; to be implemented in subclasses.
        ...
