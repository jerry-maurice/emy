from django.urls import path, include
from emmanuel import views

urlpatterns = [
    path('home/', views.user_home, name='user-home'),
    path('profile/', views.user_profile, name='user-profile'),
    path('profile/new/', views.newProfile, name='new-profile'),
    path('discover/', views.discover, name="discover"),
    path('discover/<int:user_id>/profile', views.user_selected_profile, name="user-selected-profile"),
    path('following/<int:target_id>', views.following, name="follow"),
    path('unfollowing/<int:target_id>', views.unfollowing, name="unfollow"),
    path('discovering/', views.discovering, name="discovering"),
    #path('event/<int:event_id>/', views.events_detail, name="event_detail"),
]