from django.urls import path, include
from mediaApp import views

urlpatterns = [
    path('', views.mediaView, name='media'),
]