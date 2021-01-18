from django.db import models
from django.contrib.auth.models import User
from account.models import Member

# Create your models here.


EVENT_OCCURENCES = {
    ('W',"Weekly"),
    ('D',"Daily"),
    ('M',"Monthly"),
    ('Y',"Yearly"),
}
class Event(models.Model):
    name = models.CharField(max_length=250, null=True, blank=True)
    about = models.TextField(blank=True, null=True)
    imagePoster = models.URLField(blank=True, null=True)
    imagePage = models.URLField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    occurence = models.CharField(max_length=250, choices=EVENT_OCCURENCES,default="Weekly")
    eventDate = models.DateTimeField(null=True, blank=True)
    isActive = models.BooleanField(default=True)
    price = models.FloatField(default=0)

    def __str__(self):
        return self.name


class Event_Participant(models.Model):
    '''
    list of participant
    '''
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    participant = models.ForeignKey(Member, on_delete=models.CASCADE)
    is_paid = models.BooleanField(default=False)