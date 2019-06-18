from rest_framework import serializers
from .models import *

class PickupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PickUp
        fields = ('farm', 'fish', 'quantity')