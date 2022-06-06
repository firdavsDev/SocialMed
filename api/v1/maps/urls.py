from django.urls import include, path, re_path

from .views import *

urlpatterns = [
    path("", MapsList.as_view(), name="maps-list"),
    path("<int:pk>/", MapsDetail.as_view(), name="maps-detail"),
]
