from django.urls import path, register_converter
from . import views

urlpatterns = [
    
    path('create/', views.create_post, name='create_post'),
    path('update/<int:pk>/', views.update_post, name='update_post'),
    path('delete/<int:pk>/', views.delete_post, name='delete_post'),
    path('get/<int:pk>/', views.get_post, name='get_post'),
    path('get/', views.get_posts, name='get_posts'),
   
]