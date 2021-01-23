from django.urls import path, include
from notification import views

urlpatterns = [
    path('<int:notification_id>/detail/', views.notification, name='notification-detail'),
]