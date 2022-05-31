from django.shortcuts import render

# Create your views here.
from rest_framework import generics, mixins, status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.db.models import Q, F, Value

from .models import News
from .serializers import NewsSerializer

#News list api
class NewsList(generics.ListAPIView):
    '''List all news'''
    serializer_class = NewsSerializer
    def get_queryset(self):
        return News.objects.filter(is_active=True)
    
#News detail api
class NewsDetail(generics.RetrieveAPIView):
    '''Retrieve, update or delete a news instance.'''
    serializer_class = NewsSerializer

    def get_queryset(self, *args, **kwargs):
        return News.objects.filter(pk=self.kwargs['pk'])