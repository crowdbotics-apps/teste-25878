from rest_framework import authentication
from location.models import MapLocation, ProfileLocation, VehicleLocation
from .serializers import (
    MapLocationSerializer,
    ProfileLocationSerializer,
    VehicleLocationSerializer,
)
from rest_framework import viewsets


class ProfileLocationViewSet(viewsets.ModelViewSet):
    serializer_class = ProfileLocationSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = ProfileLocation.objects.all()


class MapLocationViewSet(viewsets.ModelViewSet):
    serializer_class = MapLocationSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = MapLocation.objects.all()


class VehicleLocationViewSet(viewsets.ModelViewSet):
    serializer_class = VehicleLocationSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = VehicleLocation.objects.all()
