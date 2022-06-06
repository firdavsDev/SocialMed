from django.urls import include, path, re_path

from .views import *

urlpatterns = [
    path("", NewsList.as_view(), name="news-list"),
    path("<int:pk>/", NewsDetail.as_view(), name="news-detail"),
]
