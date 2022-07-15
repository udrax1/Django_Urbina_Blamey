from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser

from petfriends.models import Venta
from .serializers import VentaSerializer
from django.db.models import Q

# Create your views here.


@api_view(['GET', 'POST'])
def lista_venta(request):
    if request.method== 'GET':
        venta = Venta.objects.all()
        serializer = VentaSerializer(venta, many =True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = VentaSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

