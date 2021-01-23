from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
import json
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from notification.models import Notification

# Create your views here.
@login_required
def notification(request, notification_id):
    if request.method == 'GET':
        notification = get_object_or_404(Notification, pk=notification_id)
        context = {
            'notification': notification
        }
        return render(request, 'notification/notification_detail.html', context)
