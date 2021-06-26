from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404

from event.models import Event
from account.models import Member
from streamapp.models import Tweet, Item, Follow

from stream_django.enrich import Enrich
from stream_django.feed_manager import feed_manager

import logging

enricher = Enrich()
# get an instance of a logger
logger = logging.getLogger(__name__)


# member page view
@login_required
def memberHome(request):
    user = request.user
    if request.method == 'GET':
        account = get_object_or_404(Member, user=user)
        feeds = feed_manager.get_news_feeds(user.id)
        #notification_feeds = feed_manager.get_notification_feed(user.id)
        #logger.info(notification_feeds.get('notification').get()['results'])
        activities = feeds.get('timeline').get()['results']
        enriched_activities = enricher.enrich_activities(activities)
        # notification = Notification.objects.all().order_by('-id')[:10]
        context = {
            'activities':enriched_activities,
            'member':account,
            'events':Event.objects.all().filter(isActive=True),
            'members':Member.objects.all()
        }
        return render(request, 'memberApp/home.html',context)
    if request.method == 'POST':
        videos = ['avi','mp4','mov','wmv','MP4','AVI','MOV', 'WMV']
        textFeed = None
        imageFeed = None
        checkVideo = False
        #if request.POST['postFeed']:
        textFeed = request.POST['postFeed']
        if (request.FILES):
            imageFeed = request.FILES['postFeedImage']
            logger.info("image added")
            imageName= imageFeed.name
            # split name to check if it is a video
            imageNameList = imageName.split('.')
            if imageNameList[1] in videos:
                checkVideo = True
            logger.info(checkVideo)
        #item = Item(text=textFeed, image=imageFeed, author=user)
        #item.save()
        tweet = Tweet(author=user,text=textFeed, image=imageFeed, is_video=checkVideo)
        tweet.save()
        return redirect(memberHome)
