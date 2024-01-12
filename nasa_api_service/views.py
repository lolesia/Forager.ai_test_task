"""Nasa Open Api Views."""
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.serializers import ValidationError
from rest_framework.views import APIView

from nasa_api_service.dto import DateDto, GstDto
from nasa_api_service.geomagnetic_storm_service import GeomagneticStormService
from nasa_api_service.nasa_data_service import NasaGetData
from nasa_api_service.serializers import ApodDTOSerializer, DateSerializer, GstDTOSerializer


class AstronomyPictureNASAView(APIView):
    """
    API View for retrieving information about the Astronomy Picture of the Day (APOD) from NASA.

    Supports the GET HTTP method for retrieving information about the current Astronomy Picture of the Day.

    Example:
    - GET: /nasa/picture_of_the_day/

    Returns serialized ApodDTO on successful request.

    In case of an error, returns an appropriate HTTP status and an error message.

    Attributes:
    - NasaGetData: A service class for collecting data from the NASA Open API.
    - ApodDTOSerializer: Serializer class for converting ApodDTO to JSON.
    """

    def get(self, request: Request) -> Response:
        """
        Retrieve information about the current Astronomy Picture of the Day.

        :param request: Request object.
        :return: Serialized ApodDTO and HTTP status 200 on success.
        :rtype: Response
        """
        nasa_open_api = NasaGetData()
        try:
            apod_info = nasa_open_api.astronomy_picture_of_the_day_data()
        except Exception as exception:
            return Response({'error': str(exception)}, status=status.HTTP_400_BAD_REQUEST)
        apod_serializer = ApodDTOSerializer(apod_info)
        return Response(apod_serializer.data, status=status.HTTP_200_OK)


class GeomagneticStormNASAView(APIView):
    """
    API View for retrieving information about the Geomagnetic Storm (GST) from NASA.

    Supports the POST HTTP method for retrieving information about the Geomagnetic Storm for a given date period .

    Example:
    - POST: /nasa/geomagnetic_storm/
    Request Body:

          "start_date": "2022-01-01",
          "end_date": "2023-01-10"

    Returns serialized GstDTO on successful request.

    In case of an error, returns an appropriate HTTP status and an error message.

    Attributes:
    - nasa_open_api: A service class for collecting data from the NASA Open API.
    - saved_gst_data: List to store Geomagnetic Storm data.
    """

    def __init__(self) -> None:
        """
        Constructors of GeomagneticStormNASAView class.

        Initializes the class object and sets attributes:
            - nasa_open_api: An instance of NasaGetData class for accessing NASA Open API.
        """
        super().__init__()
        self.nasa_open_api = NasaGetData()

    saved_gst_data: list[GstDto] = []

    def post(self, request: Request) -> Response:
        """
        Retrieve information about the Geomagnetic Storm for a given date period.

        :param request: Request object.
        :return: Serialized GstDTO and HTTP status 200 on success.
        :rtype: Response
        """
        date_serializer = DateSerializer(data=request.data)
        if not date_serializer.is_valid():
            raise ValidationError
        date_dto = DateDto(
            start_date=date_serializer.validated_data.get('start_date'),
            end_date=date_serializer.validated_data.get('end_date'),
        )
        try:
            gst_info = self.nasa_open_api.geomagnetic_storm_data(date_dto)
        except Exception as exception:
            return Response({'error': str(exception)}, status=status.HTTP_400_BAD_REQUEST)
        self.saved_gst_data.extend(gst_info)
        gst_serializer = GstDTOSerializer(gst_info, many=True)
        return Response(gst_serializer.data, status=status.HTTP_200_OK)


class GeomagneticStormNASADetailView(APIView):
    """
    API view for retrieving, updating, and deleting a specific Geomagnetic Storm record.

    Supports the GET, PUT, DELETE HTTP method for retrieving, updating, deleting information about the Geomagnetic
    Storm from the saved_gst_data list generated by the post method in class GeomagneticStormNASAView.

    Methods:
        - GET: Retrieve a Geomagnetic Storm record by its ID.
        - PUT: Update a Geomagnetic Storm record by its ID.
        - DELETE: Delete a Geomagnetic Storm record by its ID.
    Example:
        - GET: /nasa/geomagnetic_storm/1/
        - PUT: /nasa/geomagnetic_storm/1/
        - DELETE: /nasa/geomagnetic_storm/1/

    Returns serialized GstDTO on successful request.

    Attributes:
         - get_gst_by_id: Method for retrieving a Geomagnetic Storm record by its ID.
         - update_gst_data: Method for updating a Geomagnetic Storm record by its ID.
         - delete_gst_data: Method for deleting a Geomagnetic Storm record by its ID.
         - saved_gst_data: List to store Geomagnetic Storm data.
    """

    def __init__(self) -> None:
        """
        Constructors of GeomagneticStormNASADetailView class .

        Initializes the class object and sets attributes:
            - get_gst_by_id: Method to retrieve geomagnetic storm data by identifier.
            - update_gst_data: Method to update geomagnetic storm data by identifier.
            - delete_gst_data: Method to delete geomagnetic storm data by identifier.
        """
        super().__init__()
        self.get_gst_by_id = GeomagneticStormService().get_gst_by_id
        self.update_gst_data = GeomagneticStormService().update_gst_data
        self.delete_gst_data = GeomagneticStormService().delete_gst_data

    saved_gst_data = GeomagneticStormNASAView.saved_gst_data

    def get(self, request: Request, pk: int) -> Response:
        """
        Retrieve a Geomagnetic Storm record by its ID.

        :param request: Request object.
        :param pk: ID of the Geomagnetic Storm record to retrieve.
        :return: Serialized Geomagnetic Storm record and HTTP status 200 on success.
        :rtype: Response
        """
        try:
            gst_by_id = self.get_gst_by_id(self.saved_gst_data, pk)
        except Exception as exception:
            return Response({'error': str(exception)}, status=status.HTTP_400_BAD_REQUEST)

        gst_serializer = GstDTOSerializer(gst_by_id)

        return Response(gst_serializer.data, status=status.HTTP_200_OK)

    def put(self, request: Request, pk: int) -> Response:
        """
        Update a Geomagnetic Storm record by its ID.

        :param request: Request object.
        :param pk: ID of the Geomagnetic Storm record to update.
        :return: Serialized updated Geomagnetic Storm record and HTTP status 200 on success.
        :rtype: Response
        """
        try:
            update_gst_data = self.update_gst_data(self.saved_gst_data, pk, update_gst_data=request.data)
        except Exception as exception:
            return Response({'error': str(exception)}, status=status.HTTP_400_BAD_REQUEST)

        gst_serializer = GstDTOSerializer(update_gst_data, many=True)

        return Response(gst_serializer.data, status=status.HTTP_200_OK)

    def delete(self, request: Request, pk: int) -> Response:
        """
        Delete a Geomagnetic Storm record by its ID.

        :param request: Request object.
        :param pk: ID of the Geomagnetic Storm record to delete.
        :return: Serialized updated list of Geomagnetic Storm records and HTTP status 200 on success.
        :rtype: Response
        """
        try:
            delete_gst_data = self.delete_gst_data(self.saved_gst_data, pk)
        except Exception as exception:
            return Response({'error': str(exception)}, status=status.HTTP_400_BAD_REQUEST)

        gst_serializer = GstDTOSerializer(delete_gst_data, many=True)

        return Response(gst_serializer.data, status=status.HTTP_200_OK)
