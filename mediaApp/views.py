from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
import json
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User

from mediaApp.models import medialibrary

import logging

# get an instance of a logger
logger = logging.getLogger(__name__)

# Create your views here.
def mediaView(request):
    media = medialibrary.objects.filter(is_video=False)
    video = medialibrary.objects.filter(is_video=True)
    context = {
        'media':media,
        'video':video,
    }
    return render(request, 'mediaApp/media.html',context)

