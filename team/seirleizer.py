from rest_framework.serializers import ModelSerializer
from .models import *
class TeamsSer(ModelSerializer):
    class Meta:
     model = TeamModel
     fields = ["image",'name',"id"]
class TeamSer(ModelSerializer):
    class Meta:
     model = TeamModel
     fields = "__all__"