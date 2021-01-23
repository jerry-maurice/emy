from django.contrib import admin
from event.models import Event, EVENT_OCCURENCES, Agenda

# Register your models here.
admin.site.register(Event)
admin.site.register(Agenda)