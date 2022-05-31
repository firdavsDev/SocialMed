from rest_framework import serializers

from .models import *

class ServiceCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceCategory
        fields = "__all__"


class ServiceSerializer(serializers.ModelSerializer):
    service_type = ServiceCategorySerializer(read_only=True)
    class Meta:
        model = Service
        fields = "__all__"
        read_only_fields = ['id','is_active' ,'created_at','is_free']
