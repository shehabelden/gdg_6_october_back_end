from rest_framework import mixins, generics
from .serilzer import *
from rest_framework import generics


class TiketApi(mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = TicketModel.objects.all()

    serializer_class = TiketSerilezer

    def get(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
