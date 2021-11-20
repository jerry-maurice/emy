from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User

from event.models import Event
from memberApp.models import Member
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
        if Member.objects.filter(user=user).exists():
            account = get_object_or_404(Member, user=user)
            feeds = feed_manager.get_news_feeds(user.id)
            auth0user = user.social_auth.get(provider='auth0')
            #notification_feeds = feed_manager.get_notification_feed(user.id)
            #logger.info(notification_feeds.get('notification').get()['results'])
            activities = feeds.get('timeline').get()['results']
            enriched_activities = enricher.enrich_activities(activities)
            # notification = Notification.objects.all().order_by('-id')[:10]
            context = {
                'activities':enriched_activities,
                'member':account,
                'events':Event.objects.all().filter(isActive=True),
                'members':Member.objects.all(),
                'picture':auth0user.extra_data['picture'],
            }
            return render(request, 'memberApp/home.html',context)
        else:
            return redirect(member_registration)

        
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


# member registration
def member_registration(request):
    user = request.user
    if request.method == 'GET':
        return render(request, 'memberApp/member_registration.html')
    if request.method == 'POST':
        firstName = request.POST['firstName']
        lastName = request.POST['lastName']
        dob = request.POST['dateOfBirth']
        phoneNumber = request.POST['memberNumber']
        about = request.POST["memberAbout"]

        user.first_name = firstName
        user.last_name = lastName
        user.save()

        if (request.FILES):
            memberPicture = request.FILES['memberPicture']
            member = Member(user=user, image=memberPicture, dateofbirth=dob, phone=phoneNumber, about=about)
            member.save()
        else:
            member = Member(user=user, dateofbirth=dob, phone=phoneNumber, about=about)
            member.save()
        # follow self 
        if Follow.objects.filter(user=user, target=user).exists() == False:
            follow = Follow(user=user, target=user)
            follow.save()
        # follow main user
        if User.objects.filter(email='emmanuelmaranathayouth@gmail.com').exists() == False:
            follow_priority = Follow(user=user,target=get_object_or_404(User,email='emmanuelmaranathayouth@gmail.com'))
            follow_priority.save()
        return redirect(memberHome)

