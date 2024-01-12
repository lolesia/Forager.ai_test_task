"""Data collection service with Nasa Open API Client."""

from nasa_api_service.dto import ApodDTO, DateDto, GstDto
from open_api_client.nasa_client import AstronomyPictureApiClient, GeomagneticStormApiClient


class NasaGetData(object):
    """Class to collect information from Nasa Open API Client."""

    def astronomy_picture_of_the_day_data(self) -> ApodDTO:
        """Retrieve information about the astronomy picture of the day."""
        nasa_client = AstronomyPictureApiClient()

        apod_info = nasa_client.astronomy_picture_of_the_day()

        return self.apod_data_to_dto(apod_info)

    def geomagnetic_storm_data(self, date_dto: DateDto) -> list[GstDto]:
        """Retrieve information about geomagnetic storm data."""
        nasa_client = GeomagneticStormApiClient()

        gst_info = nasa_client.geomagnetic_storm(date_dto)
        gst_filter_info = self.filter_geomagnetic_storm_data(gst_info)
        return self.gst_data_to_dto(gst_filter_info)

    def filter_geomagnetic_storm_data(self, gst_info: dict) -> list:
        """Filter geomagnetic storm data."""
        filter_data = []

        for entries_id, gst_element in enumerate(gst_info, start=1):
            item_data = {
                'pk': entries_id,
                'gst_id': gst_element.get('gstID'),
                'link': gst_element.get('link'),
                'kp_index': gst_element.get('allKpIndex')[0]['kpIndex'],
            }

            filter_data.append(item_data)
        return filter_data

    def gst_data_to_dto(self, gst_filter_info: list) -> list[GstDto]:
        """Convert geomagnetic storm information into a list of GstDto objects."""
        gst_dto_list = []
        for gst_data in gst_filter_info:
            gst_dto_list.append(GstDto(
                id=gst_data.get('pk'),
                gst_id=gst_data.get('gst_id'),
                link=gst_data.get('link'),
                kp_index=gst_data.get('kp_index'),
            ))
        return gst_dto_list

    def apod_data_to_dto(self, apod_info: dict) -> ApodDTO:
        """Convert the astronomy picture of the day information into a ApodDTO objects."""
        return ApodDTO(
            date=apod_info['date'],
            explanation=apod_info['explanation'],
            name=apod_info['title'],
            image_link=apod_info['url'],
        )
