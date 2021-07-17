from django.db import models
from django.contrib.auth.models import User
from account.models import Member

from stream_django.activity import Activity
from stream_django.feed_manager import feed_manager
from django.db.models import signals

# Create your models here.
class Item(models.Model):
    '''
    post
    '''
    text = models.TextField(blank=True, null=True)
    image = models.FileField(blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.text


class Tweet(models.Model, Activity):
    '''
    '''
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(blank=True, null=True)
    image = models.FileField(blank=True, null=True)
    is_video = models.BooleanField(default=False)

    @property
    def activity_actor_attr(self):
        return self.author
'''
    @property
    def extra_activity_data(self):
        return {'is_retweet': self.is_retweet }

    @property
    def activity_notify(self):
        if self.is_retweet and self.parent_tweet.author != self.author:
            target_feed = feed_manager.get_notification_feed(self.parent_tweet.author_id)
            return [target_feed]'''


class Comment(models.Model):
    '''
    user can comment on other user message
    '''
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(blank=True, null=True)
    tweet = models.ForeignKey(Tweet, on_delete=models.CASCADE, null=False)

    def __str__(self):
        return self.author +" - "+ self.text


class Like(models.Model):
    '''
    user can add like
    '''
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    like = models.IntegerField(default=0, null=False, blank=True)
    tweet = models.ForeignKey(Tweet, on_delete=models.CASCADE)

    def __str__(self):
        return "" +self.like
    


class Follow(models.Model):
    user = models.ForeignKey(
        User, related_name='friends', on_delete=models.CASCADE)
    target = models.ForeignKey(
        User, related_name='followers', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def activity_notify(self):
        return [feed_manager.get_notification_feed(self.target_user.id)]

    class Meta:
        unique_together = ('user', 'target')



def unfollow_feed(sender, instance, **kwargs):
    feed_manager.unfollow_user(instance.user_id, instance.target_id)


def follow_feed(sender, instance, created, **kwargs):
    if created:
        feed_manager.follow_user(instance.user_id, instance.target_id)


signals.post_delete.connect(unfollow_feed, sender=Follow)
signals.post_save.connect(follow_feed, sender=Follow)
