from django.db.models import F, Q, Value
from django.shortcuts import render

# Create your views here.
from rest_framework import generics, mixins, status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import News
from .serializers import NewsSerializer


# News list api
class NewsList(generics.ListAPIView):
    """List all news"""

    serializer_class = NewsSerializer

    def get_queryset(self):
        return News.objects.filter(is_active=True)


# News detail api
class NewsDetail(generics.RetrieveAPIView):
    """Retrieve, update or delete a news instance."""

    serializer_class = NewsSerializer
    queryset = News.objects.all()
    # permission_classes = []

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset()
        queryset.filter(pk=self.kwargs.get("pk")).update(
            views_count=F("views_count") + 1
        )
        return queryset
