from rest_framework import viewsets
from devices.api import serializers
from devices import models

class DevicesViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.DevicesSerializer
    queryset = models.Devices.objects.all()