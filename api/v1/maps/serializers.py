from rest_framework import serializers

from .models import *


class MapCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryofMaps
        fields = "__all__"


class MapsSerializer(serializers.ModelSerializer):
    category = MapCategorySerializer(read_only=True)

    class Meta:
        model = Maps
        fields = "__all__"
        read_only_fields = ["id", "is_active", "created_at"]
