from rest_framework import mixins, generics
from .seirlzer import *


class HomeApi(mixins.ListModelMixin , generics.GenericAPIView):

    queryset = HomeBadge.objects.all()

    serializer_class = HomeSerializer

    # permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
