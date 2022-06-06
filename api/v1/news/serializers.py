from rest_framework import serializers

from .models import *


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = "__all__"
        read_only_fields = ["id", "is_active", "created_at"]
