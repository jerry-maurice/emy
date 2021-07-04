from django.urls import path
from memberApp import views

urlpatterns = [
    path('home/', views.memberHome, name='member'),
    path('registration/', views.member_registration, name='memberRegistration'),
]