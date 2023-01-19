from rest_framework import mixins,generics
from .seirleizer import *
class TeamsApi(mixins.ListModelMixin,generics.GenericAPIView):
    queryset = TeamModel.objects.all()
    serializer_class = TeamsSer
    # permission_classes = (IsAuthenticated,)
    def get(self,request,*args,**kwargs):
      return  self.list(request, *args, **kwargs)
class TeamApi(mixins.RetrieveModelMixin,generics.GenericAPIView):
    queryset = TeamModel.objects.all()
    serializer_class = TeamSer
    lookup_field = "id"
    # permission_classes = (IsAuthenticated,)
    def get(self,request,*args,**kwargs):
      return  self.retrieve(request, *args, **kwargs)