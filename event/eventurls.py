from django.urls import path
from .api import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('event/<int:id>', EventApi.as_view()),
    path('', EventsApi.as_view()),
    path('tokes', TokesApi.as_view()),
    path('toke/<int:id>', TokeApi.as_view()),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)