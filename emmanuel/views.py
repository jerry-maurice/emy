from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
import json
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User

from stream_django.enrich import Enrich
from stream_django.feed_manager import feed_manager

from event.models import Event
from account.models import Member
from streamapp.models import Tweet, Item, Follow
from notification.models import Notification
import logging
from django.http import JsonResponse
from django.db.models import Q
from django.core.serializers import serialize

enricher = Enrich()
# get an instance of a logger
logger = logging.getLogger(__name__)

# Create your views here.
def home(request):
    return render(request, 'emmanuel/index.html')

@login_required
def user_home(request):
    user = request.user
    if request.method == 'GET':
        if not Member.objects.filter(user=user).exists():
            return redirect(newProfile)
        account = get_object_or_404(Member, user=user)
        feeds = feed_manager.get_news_feeds(user.id)
        #notification_feeds = feed_manager.get_notification_feed(user.id)
        #logger.info(notification_feeds.get('notification').get()['results'])
        activities = feeds.get('timeline').get()['results']
        enriched_activities = enricher.enrich_activities(activities)
        notification = Notification.objects.all().order_by('-id')[:10]
        context = {
            'activities':enriched_activities,
            'member':account,
            'notifications':notification,
        }
        return render(request, 'emmanuel/home.html',context)
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
        return redirect(user_home)


@login_required
def user_profile(request):
    user = request.user
    if request.method == 'GET':
        if not Member.objects.filter(user=user).exists():
            return redirect(newProfile)
        feeds = feed_manager.get_user_feed(user.id)
        activities = feeds.get()['results']
        enriched_activities = enricher.enrich_activities(activities)
        notification = Notification.objects.all().order_by('-id')[:10]
        context = {
            'activities':enriched_activities,
            'member':get_object_or_404(Member, user=user),
            'notifications':notification,
        }
        return render(request, 'emmanuel/profile.html',context)


@login_required
def newProfile(request):
    user = request.user
    if request.method == 'GET':
        return render(request, 'account/profile_form.html')
    if request.method == 'POST':
        profileImage = None
        if request.FILES:
            profileImage = request.FILES['profile_picture']
        profileDob = request.POST['profile_dob']
        about = request.POST['profile_about']
        if not Member.objects.filter(user=user).exists():
            member = Member(user=user, image=profileImage, dateofbirth=profileDob, about=about)
            member.save()
            follow = Follow(user=user, target=user)
            follow.save()
        return redirect(user_profile)


@login_required
def discover(request):
    user = request.user
    if request.method == 'GET':
        if not Member.objects.filter(user=user).exists():
            return redirect(newProfile)
        account = get_object_or_404(Member, user=user)
        members = Member.objects.all()
        notification = Notification.objects.all().order_by('-id')[:10]
        context = {
            'member':account,
            'members':members,
            'notifications':notification,
        }
        return render(request, 'emmanuel/discover.html',context)


@login_required
def user_selected_profile(request, user_id):
    user = request.user
    if request.method == 'GET':
        if not Member.objects.filter(user=user).exists():
            return redirect(newProfile)
        feeds = feed_manager.get_user_feed(user_id)
        activities = feeds.get()['results']
        enriched_activities = enricher.enrich_activities(activities)
        notification = Notification.objects.all().order_by('-id')[:10]
        context = {
            'activities':enriched_activities,
            'member':get_object_or_404(Member, user=get_object_or_404(User, id=user_id)),
            'follow':Follow.objects.filter(user=user, target=get_object_or_404(User, id=user_id)).exists(),
            'notifications':notification,
        }
        return render(request, 'emmanuel/profile_user.html',context)

        
@login_required
def following(request,target_id):
    user = request.user
    target = get_object_or_404(User, id=target_id)
    if request.method == 'GET':
        follow = Follow(user=user, target=target)
        follow.save()
        return redirect(discover)

        
@login_required
def unfollowing(request,target_id):
    user = request.user
    target = get_object_or_404(User, id=target_id)
    if request.method == 'GET':
        follow = get_object_or_404(Follow, user=user, target=target)
        follow.delete()
        return redirect(discover)

        
@login_required
def discovering(request):
    if request.is_ajax():
        #follower = serialize("json",Follow.objects.filter(target=request.user).count())
        #following = serialize("json",Follow.objects.filter(user=request.user).count())
        data = {
            'follower':Follow.objects.filter(target=request.user).count(),
            'following':Follow.objects.filter(user=request.user).count(),
        }
        return JsonResponse(data, safe=False)

'''
@login_required
def home(request):
    
    #first page when a user open EMY
    
    committee = Members.objects.all().filter(isInCommittee=True)
    context = {
        'committee':committee
    }
    return render(request, 'emmanuel/home.html', context)






'''
    
