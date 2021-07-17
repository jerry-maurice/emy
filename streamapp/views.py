from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User

from django.http import JsonResponse

from streamapp.models import Tweet, Item, Follow, Like, Comment

import logging, json


# get an instance of a logger
logger = logging.getLogger(__name__)


# number of likes in a post
@login_required
def getNumberLike(request, id):
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        if request.method == 'GET':
            tweet = get_object_or_404(Tweet, id=id)
            like = Like.objects.filter(tweet=tweet)
            comment = Comment.objects.filter(tweet=tweet)
            if like is not None and comment is not None:
                count_like = len(like)
                count_comment = len(comment)
            elif like is not None and comment is None:
                count_like = len(like)
                count_comment =0
            elif like is None and comment is not None:
                count_like = 0
                count_comment = len(comment)
            else:
                count_like = 0
                count_comment = 0

            data = {
                'likes':count_like,
                'comments':count_comment
            }
            return JsonResponse(data)
            
        if request.method == 'POST':
            data_from_post = json.load(request)['post_data']
            logger.info(data_from_post)
            tweet = get_object_or_404(Tweet, id=id)
            logger.info(Like.objects.filter(tweet=tweet, author=request.user).exists())
            if Like.objects.filter(tweet=tweet, author=request.user).exists() == False:
                like = Like(tweet=tweet, author=request.user, like=1)
                like.save()
            else:
                Like.objects.filter(tweet=tweet, author=request.user).delete()
            
            like = Like.objects.filter(tweet=tweet)
            if like is not None:
                count = len(like)
            else:
                count = 0
            data = {
                'likes':count
            }
            return JsonResponse(data)


# single comment
@login_required
def socialInterraction(request, id):
    tweet = get_object_or_404(Tweet, id=id)
    if request.method == 'GET':
        comments = Comment.objects.filter(tweet=tweet)
        context = {
            'tweet':tweet,
            'comments':comments,
        }
        return render(request, 'streamapp/comment.html', context)
    if request.method == 'POST':
        text = request.POST['comment']
        comment = Comment(author=request.user, text=text, tweet=tweet)
        comment.save()
        comments = Comment.objects.filter(tweet=tweet)
        context = {
            'tweet':tweet,
            'comments':comments,
        }
        return render(request, 'streamapp/comment.html', context)
            