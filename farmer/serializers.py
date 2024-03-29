from rest_framework import serializers
from .models import *

class PickupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PickUp
        fields = ('id','farm', 'fish', 'quantity','status')

class FarmSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Farm
        fields = ('id', 'farm_name',)
