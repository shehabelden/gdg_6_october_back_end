from django.urls import path
from .api import *
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('team/<int:id>', TeamApi.as_view()),
    path("", TeamsApi.as_view()),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)