from django.shortcuts import render, redirect
from event.models import Event

import logging

# get an instance of a logger
logger = logging.getLogger(__name__)

'''
    home view. first page a user will 
'''
def homeView(request):
    logger.info("user in index page")
    events = Event.objects.all().filter(isActive=True)
    context = {
        'events':events,
    }
    return(request, 'home/index.html', context)