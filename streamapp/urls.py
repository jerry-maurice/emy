from django.urls import path
from streamapp import views

urlpatterns = [
    path('likes/<int:id>', views.getNumberLike, name='likes'),
    path('tweet/<int:id>', views.socialInterraction, name='interraction'),
]