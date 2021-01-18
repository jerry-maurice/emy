from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
import json
from django.http import HttpResponseRedirect
from event.models import Event
from contest.models import Videolibrary
import logging

# Create your views here.
@login_required
def events(request):
    '''
    list of events
    '''
    events = Event.objects.all().filter(isActive=True)
    context = {
        'events':events,
    }
    return render(request, 'event/events.html', context)


@login_required
def events_detail(request,event_id):
    '''
    specific event
    '''
    event = get_object_or_404(Event,pk=event_id)
    if event.occurence == 'Y':
        videos = Videolibrary.objects.all()
        context = {
            'event':event,
            'videos':videos,
        }
        return render(request,'emmanuel/christmas_contest.html',context)
    elif event.occurence == 'W':
        context = {
            'event':event,
        }
        return render(request,'emmanuel/event_detail.html',context)