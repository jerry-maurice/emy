from django.urls import path, include
from auth0login import views

urlpatterns = [
    path('', views.index),
    path('user-logout/', views.logout),
    path('', include('django.contrib.auth.urls')),
    path('', include('social_django.urls')),
]