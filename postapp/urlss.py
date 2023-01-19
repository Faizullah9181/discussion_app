from django.urls import path
from . import views

urlpatterns = [

    
    path('create/', views.create_comment, name="create-comment"),
    path('get/', views.get_comments, name="get-comments"),

   
]