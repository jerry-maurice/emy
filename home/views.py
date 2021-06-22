from django.shortcuts import render, redirect

import logging

# get an instance of a logger
logger = logging.getLogger(__name__)

'''
    home view. first page a user will 
'''
def homeView(request):
    logger.info("user in home page")
    return(request, 'home/index.html')