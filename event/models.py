from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from home_badge.models import HomeBadge


class TopicModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=40, default="s")
    topic = models.CharField(max_length=400, default="s")
    image = models.ImageField()
    bio = models.CharField(max_length=4000)
    date = models.DateField(auto_now=True)
    start = models.DateField(auto_now=True)
    end = models.DateField(auto_now=True)


class EventModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=40, default="s")
    image = models.ImageField()
    bio = models.CharField(max_length=4000)
    date = models.DateField(auto_now=True)
    start = models.DateField(auto_now=True)
    end = models.DateField(auto_now=True)
    topic = models.ManyToManyField(TopicModel)
    avilabolevent = models.BooleanField(default=True)


@receiver(post_save, sender=User)
def carearte(sender, instance, created, **kwargs):
    if created:
        HomeBadge.objects.create(
            user=EventModel.user,
            title=EventModel.name,
            image=EventModel.image,
            topic="event"
        )
