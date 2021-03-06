from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import get_object_or_404, render
import json
from django.http import HttpResponseRedirect
from contest.models import Videolibrary, Rating, Like

# Create your views here.
@staff_member_required
def round(request):
    '''
    display contest round
    '''
    if request.method == 'GET':
        return render(request, 'contest/round.html')


@staff_member_required
def videosContest(request, round_id):
    '''
    list of videos for the round selected
    '''
    if request.method == 'GET':
        videos = Videolibrary.objects.all().filter(roundNumber=round_id)
        context = {
            'videos':videos,
        }
        return render(request, 'contest/videos.html', context)


@staff_member_required
def score(request, video_id):
    video = get_object_or_404(Videolibrary, pk=video_id)
    user = request.user
    if request.method == 'GET':
        context={
            'video':video,
        }
        return render(request, 'contest/score.html', context)
    if request.method == 'POST':
        performance = request.POST['performance']
        choice = request.POST['choice']
        ontime = request.POST['ontime']
        presentation = request.POST['presentation']
        confidence = request.POST['confidence']
        comment = request.POST['comment']
        rate = Rating(performance=performance, choice=choice, ontime=ontime, presentation=presentation, confidence=confidence, judge=user,video=video, comment=comment)
        if Rating.objects.filter(judge=user,video=video).exists() == False:
            rate.save()
            return redirect(round)
        else:
            message = "You already gave this video a score. Please contact support if you want to modify your score"
            context={
                'message':message,
                'video':video
            }
            return render(request, 'contest/score.html', context)


