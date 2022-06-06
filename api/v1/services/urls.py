from django.urls import include, path, re_path

from .views import *

urlpatterns = [
    path("", ServiceList.as_view(), name="maps-list"),
    path("<int:pk>/", ServiceDetail.as_view(), name="maps-detail"),
]
