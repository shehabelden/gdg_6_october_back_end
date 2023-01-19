from rest_framework.serializers import ModelSerializer
from .models import *
from tiket.models import TicketModel
class TopicsSer(ModelSerializer):
    class Meta:
     model = TopicModel
     fields = ["name", "id", "image",
               "date" , "start" , "end" , ]
class TopicSer(ModelSerializer):
    class Meta:
     model = TopicModel
     fields = ["image" , "name" , "bio", "topic"]
class TiketSerializers(ModelSerializer):
    class Meta:
        model = TicketModel
        fields = '__all__'
class EventSer(ModelSerializer):
    topic = TopicsSer(many=True)
    event = TiketSerializers(many = True )

    class Meta:

     model = EventModel
     fields = ["name" , "image" , "topic","event","avilabolevent"]
class EventsSer(ModelSerializer):
    class Meta:

     model  = EventModel
     fields = ["name" , "id", "image",
               "date" , "start" , "end" , "avilabolevent" , ]