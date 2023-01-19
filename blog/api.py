from rest_framework import mixins,generics
from .seirleizer import *
class MainBlogApi(mixins.ListModelMixin,generics.GenericAPIView):
    queryset = MainBlogModel.objects.all()
    serializer_class =MainBlogSer
    # permission_classes = (IsAuthenticated,)
    def get(self,request,*args,**kwargs):
      return  self.list(request, *args, **kwargs)
class AllBlogApi(mixins.ListModelMixin,generics.GenericAPIView):
    queryset = BlogModel.objects.all()
    serializer_class =BlogSer
    # permission_classes = (IsAuthenticated,)
    def get(self,request,*args,**kwargs):
      return  self.list(request, *args, **kwargs)
class OneBlogApi(mixins.RetrieveModelMixin,generics.GenericAPIView):
    queryset = BlogModel.objects.all()
    serializer_class =OneBlogSer
    lookup_field = "id"
    # permission_classes = (IsAuthenticated,)
    def get(self,request,*args,**kwargs):
      return  self.retrieve(request, *args, **kwargs)