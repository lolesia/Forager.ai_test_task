"""service for managing Geomagnetic Storm data."""
from nasa_api_service.dto import GstDto


class GeomagneticStormService(object):
    """
    Service class for managing Geomagnetic Storm data.

    Methods:
        - get_gst_by_id(saved_gst_data: List[GstDto], pk: int) -> GstDto:
            Retrieves Geomagnetic Storm data by its ID.

        - update_gst_data(saved_gst_data: List[GstDto], pk: int, update_gst_data: Dict) -> List[GstDto]:
            Updates Geomagnetic Storm data by its ID with the provided values.

        - delete_gst_data(saved_gst_data: List[GstDto], pk: int) -> List[GstDto]:
            Deletes Geomagnetic Storm data by its ID.
    """

    def get_gst_by_id(self, saved_gst_data: list, pk: int) -> list:
        """Retrieve Geomagnetic Storm data by its ID."""
        for gst_data in saved_gst_data:
            if gst_data.id == pk:
                return gst_data
        raise IndexError('Geomagnetic storm  with id {0} not found.'.format(pk))

    def update_gst_data(self, saved_gst_data: list[GstDto], pk: int, update_gst_data: dict) -> list[GstDto]:
        """Update Geomagnetic Storm data by its ID with the provided values."""
        gst_dto = self.get_gst_by_id(saved_gst_data, pk)

        updated_gst_object = GstDto(**{**gst_dto.__dict__, **update_gst_data})

        for index, gst_obj in enumerate(saved_gst_data):
            if gst_obj.id == pk:
                saved_gst_data[index] = updated_gst_object
                break

        return saved_gst_data

    def delete_gst_data(self, saved_gst_data: list[GstDto], pk: int) -> list[GstDto]:
        """Delete Geomagnetic Storm data by its ID."""
        for index, gst_obj in enumerate(saved_gst_data):
            if gst_obj.id == pk:
                saved_gst_data.pop(index)
                break

        return saved_gst_data
