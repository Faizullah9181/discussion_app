from django.urls import path
from .. import views

urlpatterns = [
    path('get/', views.get_notifications, name="notification"),
    path('set/', views.notification_read, name="notification_read"),
    path('delete/', views.notification_delete, name="notification_delete"),
    path('delete_all/', views.delete_all_notifications, name="notification_delete_all"),
]