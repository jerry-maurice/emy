from django.shortcuts import render, redirect
from event.models import Event

import logging
from django.core.mail import send_mail

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


'''
email  
'''
def contactForm(request):
    if request.method == 'POST':
        formName = request.POST['form-name']
        formEmail = request.POST['form-email']
        formSubject = request.POST['form-subject']
        formMessage = request.POST['form-message']

        send_mail(formSubject+' - '+formName, formMessage, formEmail, ['emmanuelmaranathayouth@gmail.com'])
        return redirect(homeView)
        