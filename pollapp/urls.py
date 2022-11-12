from django.urls import path
from . import views


urlpatterns = [
    path('create/', views.create_poll, name='create_poll'),
    path('get_polls/', views.get_polls, name='get_polls'),
    path('create_poll_option/', views.create_poll_option, name='create_poll_option'),
    path('vote_poll/', views.vote_poll, name='vote_poll'),
]