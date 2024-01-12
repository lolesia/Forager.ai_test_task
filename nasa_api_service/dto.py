"""Data Transfer Object for Nasa Open API service."""
from dataclasses import dataclass
from datetime import date


@dataclass(frozen=True)
class DateDto(object):
    """DTO for date."""

    start_date: date | None
    end_date: date | None


@dataclass(frozen=True)
class ApodDTO(object):
    """DTO for astronomy picture of the day data."""

    date: date
    explanation: str
    name: str
    image_link: str


@dataclass(frozen=True)
class GstDto(object):
    """DTO for geomagnetic_storm data."""

    id: int
    gst_id: str
    link: str
    kp_index: str
