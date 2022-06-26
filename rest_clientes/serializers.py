from rest_framework import serializers
from petfriends.models import Cliente

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model= Cliente
        fields = ['rut','nombreCliente','correo','telefono','direccion','region','imagenCli']