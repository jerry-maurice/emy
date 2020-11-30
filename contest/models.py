from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Videolibrary(models.Model):
    title = models.CharField(null=True, blank=True, max_length=250)
    url = models.URLField(null=False, blank=True)
    roundNumber = models.IntegerField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_video', null=True, blank=True)

    def __str__(self):
        return self.title
    


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_like')
    video = models.ForeignKey(Videolibrary, on_delete=models.CASCADE, related_name='video_like')
    liked = models.BooleanField(default=False)
    liking = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.liking


class Rating(models.Model):
    performance = models.IntegerField(null=True, blank=True)
    confidence = models.IntegerField(null=True, blank=True)
    choice = models.IntegerField(null=True, blank=True)
    presentation = models.IntegerField(null=True, blank=True)
    ontime = models.IntegerField(null=True, blank=True)
    video = models.ForeignKey(Videolibrary, on_delete=models.CASCADE, related_name='video_rating')
    judge = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_rating')
    added = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return self.judge.first_name
    
    @property
    def average(self):
        return float((self.presentation + self.confidence + self.choice + self.presentation + self.ontime)/5)



