from django.urls import path, include
from contest import views

urlpatterns = [
    path('round/', views.round, name="round"),
    path('round/<int:round_id>/videos', views.videosContest, name="round-videos"),
    path('score/<int:video_id>', views.score, name="score"),
]