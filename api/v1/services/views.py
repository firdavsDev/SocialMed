from django.db.models import F, Q, Value
from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Service, ServiceCategory
from .serializers import ServiceSerializer


# Service list api
class ServiceList(generics.ListAPIView):
    """List all Service"""

    serializer_class = ServiceSerializer

    def get_queryset(self):
        return Service.objects.filter(is_active=True)


# Service detail api
class ServiceDetail(generics.RetrieveAPIView):
    """Retrieve, update a Service instance."""

    serializer_class = ServiceSerializer

    def get_queryset(self, *args, **kwargs):
        return Service.objects.filter(is_active=True)
