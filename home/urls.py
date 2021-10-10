from django.urls import path
from home import views

urlpatterns = [
    path('', views.homeView, name='home'),
    path('contact', views.contactForm, name='contact'),
]