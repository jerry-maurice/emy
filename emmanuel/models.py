from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Members(models.Model):
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE, related_name='user_members',)
    image = models.URLField(blank=True, null=True)
    dateofbirth = models.DateField(null=True, blank=True)
    isInCommittee = models.BooleanField(default=False)
    title = models.CharField(max_length=250, null=True, blank=True)
    firstName = models.CharField(max_length=250, null=True, blank=True)
    lastName = models.CharField(max_length=250, null=True, blank=True)

    def __str__(self):
        return self.firstName

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

    def __str__(self):
        return self.name