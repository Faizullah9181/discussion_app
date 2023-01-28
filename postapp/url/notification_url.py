from django.urls import path
from .. import views

urlpatterns = [
    path('get/', views.get_notifications, name="notification"),
    path('set/', views.notification_read, name="notification_read"),
]