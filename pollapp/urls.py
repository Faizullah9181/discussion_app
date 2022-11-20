from django.urls import path
from . import views


urlpatterns = [
    path('create/', views.create_poll, name='create_poll'),
    path('getPoll/<int:poll_id>/', views.get_poll, name='get_poll'),
    path('getUserPolls/', views.get_user_polls, name='get_user_polls'),
    path('deletePoll/<int:poll_id>/', views.delete_poll, name='delete_poll'),
    path('getallPolls/', views.get_all_polls, name='get_all_polls'),
]