from django.contrib.auth.models import User
from django.db import models


class HomeBadge(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=40,)
    slug = models.IntegerField(default=0)
    image = models.ImageField()
    TOPIC = (("event", "event"), ("blog", "blog"), ("topic", "topic"))
    topic = models.CharField(
        max_length=40,
        choices=TOPIC,
        default="event",
    )
