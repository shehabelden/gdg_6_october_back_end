from django.urls import path
from .api import *

urlpatterns = [
    path("", TiketApi.as_view())
]