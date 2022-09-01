from django.shortcuts import render
from aeropuerto_app.models import *
from aeropuerto_app.serializers import *
from rest_framework import viewsets, status
# Create your views here.

class Usuario_view(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = Usuario_Serializer

class Avion_view(viewsets.ModelViewSet):
    queryset = Avion.objects.all()
    serializer_class = Avion_Serializer

class Piloto_view(viewsets.ModelViewSet):
        queryset = Piloto.objects.all()
        serializer_class = Piloto_Serializer

class Vuelo_view(viewsets.ModelViewSet):
    queryset = Vuelo.objects.all()
    serializer_class = Vuelo_Serializer

class Tripulacion_view(viewsets.ModelViewSet):
    queryset = Tripulacion.objects.all()
    serializer_class =Tripulacion_Serializer

class Itinerario_view(viewsets.ModelViewSet):
    queryset = Itinerario.objects.all()
    serializer_class = Itinerario_Serializer

