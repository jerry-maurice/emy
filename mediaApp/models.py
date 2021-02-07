from django.db import models
from django.contrib.auth.models import User
from event.models import Event

# Create your models here.

class medialibrary(models.Model):
    title = models.CharField(null=True, blank=True, max_length=250)
    description = models.TextField(null=True)
    image = models.FileField(blank=True, null=True)
    is_video = models.BooleanField(default=False)
    is_support = models.BooleanField(default=False)
    event = models.ForeignKey(Event, on_delete=models.CASCADE, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title