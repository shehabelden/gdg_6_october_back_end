from django.db import models
from django.contrib.auth.models import User

from event.models import EventModel


class TicketModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT, null=True , blank=True)
    name = models.TextField(default="inter your name")
    city = models.TextField(default="city")
    email = models.EmailField()
    phone = models.CharField(max_length=12)
    Gender = (("man", "man"), ("woman", "woman"),)
    gender = models.CharField(
        max_length=40,
        choices=Gender,
        default="man",
    )
    events = models.ForeignKey(EventModel , on_delete=models.CASCADE, related_name='event')

