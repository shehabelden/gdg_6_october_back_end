from rest_framework.serializers import ModelSerializer
from .models import *


class HomeSerializer(ModelSerializer):
    class Meta:
        model = HomeBadge
        fields = "__all__"
