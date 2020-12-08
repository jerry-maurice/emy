from django.urls import path, include
from emmanuel import views

urlpatterns = [
    path('about/', views.home, name="home"),
    path('events/', views.events, name="event"),
    path('event/<int:event_id>/', views.events_detail, name="event_detail"),
]