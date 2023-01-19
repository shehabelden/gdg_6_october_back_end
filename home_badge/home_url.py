from django.urls import path
from .api import *
urlpatterns = [
    path("post", HomeApi.as_view())
]