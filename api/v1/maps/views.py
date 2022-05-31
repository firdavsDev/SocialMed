from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from django.db.models import Q, F, Value

from .models import Maps
from .serializers import MapsSerializer

#Maps list api
class MapsList(generics.ListAPIView):
    '''List all Maps'''
    serializer_class = MapsSerializer
    def get_queryset(self):
        return Maps.objects.filter(is_active=True)
    
#Maps detail api
class MapsDetail(generics.RetrieveAPIView):
    '''Retrieve, update a Maps instance.'''
    serializer_class = MapsSerializer

    def get_queryset(self, *args, **kwargs):
        return Maps.objects.filter(pk=self.kwargs['pk'])