from django.contrib import admin
from .models import *
from tiket.models import TicketModel
admin.site.register(TopicModel)

class TiketAdmin(admin.StackedInline):
    model = TicketModel
class EventAdmin(admin.ModelAdmin):
    inlines = [TiketAdmin]

admin.site.register(EventModel, EventAdmin)
# Register your models here.
