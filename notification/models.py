from django.db import models
from django.contrib.auth.models import User
from account.models import Member

# Create your models here.
class Notification(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    title = models.CharField(null=False, max_length=500)
    message = models.TextField(null=False)
    is_active = models.BooleanField(default=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return "%s %s" %(self.title, self.created)
