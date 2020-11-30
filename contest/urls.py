from django.urls import path, include
from contest import views

urlpatterns = [
    path('home/', views.home, name="home"),
    path('score/<int:video_id>', views.score, name="score"),
]