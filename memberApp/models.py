from django.db import models
from phone_field import PhoneField
from django.contrib.auth.models import User

# Create your models here.
class Member(models.Model):
    '''
    member page
    '''
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE, related_name='registered_user',)
    #image = models.FileField(blank=True, null=True)
    dateofbirth = models.DateField(null=True, blank=True)
    isInCommittee = models.BooleanField(default=False)
    title = models.CharField(max_length=250, null=True, blank=True)
    about = models.TextField(blank=True, null=True)
    phone = PhoneField(blank=True, null=True, help_text="Contact phone number")

    def __str__(self):
        return "%s, %s" % (self.user.first_name, self.user.last_name)

    class Meta:
        ordering = ['user']