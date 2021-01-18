from django.urls import path, include
from event import views

urlpatterns = [
    path('', views.events, name="event"),
    path('event/<int:event_id>/', views.events_detail, name="event_detail"),
]