"""Data Transfer Object for Nasa Open API request parameters."""
from dataclasses import dataclass


@dataclass(frozen=True)
class RequestDTO(object):
    """DTO for request parameters."""

    method: str
    base_url: str
    endpoint: str
    request_params: dict | None
    headers: dict | None
    body: dict | None
