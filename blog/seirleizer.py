from rest_framework.serializers import ModelSerializer
from .models import *
class BlogSer(ModelSerializer):
    class Meta:
     model = BlogModel
     fields = "__all__"
class MainBlogSer(ModelSerializer):
    blog=BlogSer(many=True)
    class Meta:
     model = MainBlogModel
     fields = "__all__"
class OneBlogSer(ModelSerializer):
    class Meta:
     model = BlogModel
     fields = "__all__"
