from django.urls import path
from .api import *
urlpatterns = [
    path('Registration/', RegistrationAPI.as_view()),
    path('login', LoginAPI.as_view()),
]
