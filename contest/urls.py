from django.urls import path, include
from contest import views

urlpatterns = [
    path('score/<int:video_id>', views.score, name="score"),
]