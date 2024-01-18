"""service for managing Interplanetary Shock data."""
from nasa_api_service.dto import IPSDto


class InterplanetaryShockService(object):
    """
    Service class for managing Interplanetary Shock data.

    Methods:
        - get_ips_by_id(saved_gst_data: List[IPSDto], pk: int) -> IPSDto:
            Retrieves Interplanetary Shock data by its ID.

        - update_ips_data(saved_ips_data: List[IPSDto], pk: int, update_ips_data: Dict) -> List[IPSDto]:
            Updates Interplanetary Shock data by its ID with the provided values.

        - delete_gst_data(saved_ips_data: List[IPSDto], pk: int) -> List[IPSDto]:
            Deletes Interplanetary Shock data by its ID.
    """

    def get_ips_by_id(self, saved_ips_data: list, pk: int) -> list:
        """Retrieve Interplanetary Shock data by its ID."""
        for ips_data in saved_ips_data:
            if ips_data.id == pk:
                return ips_data
        raise IndexError('Interplanetary Shock  with id {0} not found.'.format(pk))

    def update_ips_data(self, saved_ips_data: list[IPSDto], pk: int, update_ips_data: dict) -> list[IPSDto]:
        """Update Interplanetary Shock data by its ID with the provided values."""
        ips_dto = self.get_ips_by_id(saved_ips_data, pk)

        updated_gst_object = IPSDto(**{**ips_dto.__dict__, **update_ips_data})

        for index, ips_obj in enumerate(saved_ips_data):
            if ips_obj.id == pk:
                saved_ips_data[index] = updated_gst_object
                break

        return saved_ips_data

    def delete_ips_data(self, saved_ips_data: list[IPSDto], pk: int) -> list[IPSDto]:
        """Delete Interplanetary Shock data by its ID."""
        for index, ips_obj in enumerate(saved_ips_data):
            if ips_obj.id == pk:
                saved_ips_data.pop(index)
                break

        return saved_ips_data
