"""Data collection service with Nasa Open API Client."""

from nasa_api_service.dto import ApodDTO, DateDto, IPSDto
from open_api_client.nasa_client import NasaOpenApiClient


class NasaGetData(object):
    """Class to collect information from Nasa Open API Client."""

    def astronomy_picture_of_the_day_data(self) -> ApodDTO:
        """Retrieve information about the astronomy picture of the day."""
        nasa_client = NasaOpenApiClient()

        apod_info = nasa_client.apod.retrieve_endpoint_data()

        return self.apod_data_to_dto(apod_info)

    def interplanetary_shock_data(self, date_dto: DateDto) -> list[IPSDto]:
        """Retrieve information about interplanetary shock data."""
        nasa_client = NasaOpenApiClient()

        ips_info = nasa_client.ips.retrieve_endpoint_data(date_dto)
        ips_filter_info = self.filter_interplanetary_shock_data(ips_info)
        return self.ips_data_to_dto(ips_filter_info)

    def filter_interplanetary_shock_data(self, ips_info: dict) -> list:
        """Filter interplanetary shock data."""
        filter_data = []

        for entries_id, ips_element in enumerate(ips_info, start=1):
            item_data = {
                'pk': entries_id,
                'activity_id': ips_element.get('activityID'),
                'location': ips_element.get('location'),
                'link': ips_element.get('link'),
            }

            filter_data.append(item_data)
        return filter_data

    def ips_data_to_dto(self, ips_filter_info: list) -> list[IPSDto]:
        """Convert interplanetary shock information into a list of IPSDto objects."""
        ips_dto_list = []
        for ips_data in ips_filter_info:
            ips_dto_list.append(IPSDto(
                id=ips_data.get('pk'),
                activity_id=ips_data.get('activity_id'),
                location=ips_data.get('location'),
                link=ips_data.get('link'),
            ))
        return ips_dto_list

    def apod_data_to_dto(self, apod_info: dict) -> ApodDTO:
        """Convert the astronomy picture of the day information into a ApodDTO objects."""
        return ApodDTO(
            date=apod_info['date'],
            explanation=apod_info['explanation'],
            name=apod_info['title'],
            image_link=apod_info['url'],
        )
