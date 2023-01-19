from .models import *
from django.db.models.signals import post_save, pre_delete


def carearte(sender, instance, created, **kwargs):
    if created:
        HomeBadge.objects.create(user=instance.user, title=instance.name, image=instance.image, topic="event" )

post_save.connect(carearte , sender = EventModel)