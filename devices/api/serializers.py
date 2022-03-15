#from attr import field
from rest_framework import serializers
from devices import models


class DevicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Devices
        fields = '__all__'