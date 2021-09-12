from rest_framework import routers, serializers, viewsets
from .models import House

class HouseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = House
        fields = ['name', 'descrip']

