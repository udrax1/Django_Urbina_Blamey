from rest_framework import serializers
from petfriends.models import Venta

class VentaSerializer(serializers.ModelSerializer):
    class Meta:
        model= Venta
        fields = ['id_venta','cliente_rut','total','fecha','estado']  