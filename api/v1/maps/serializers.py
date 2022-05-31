from rest_framework import serializers

from .models import *

class MapsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Maps
        fields = "__all__"
        read_only_fields = ['id','is_active' ,'created_at']
