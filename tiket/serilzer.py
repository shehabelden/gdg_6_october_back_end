from .models import *
from rest_framework.serializers import ModelSerializer


class EventSer(ModelSerializer):
    class Meta:
        model = EventModel
        fields = ["name" , "image"]


class TiketSerilezer(ModelSerializer):
    # event = EventSer(many=True)

    class Meta:
        model = TicketModel
        fields = "__all__"