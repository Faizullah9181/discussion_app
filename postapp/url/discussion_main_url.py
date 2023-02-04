from ..views import get_all_post_poll
from django.urls import path

urlpatterns = [
    path('get/', get_all_post_poll, name="get_all_post_poll"),
]