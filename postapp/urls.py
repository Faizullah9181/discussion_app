from django.urls import path
from . import views

urlpatterns = [

    path('create/', views.create_post, name='create_post'),
    path('update/<int:pk>/', views.update_post, name='update_post'),
    path('delete/<int:pk>/', views.delete_post, name='delete_post'),
    path('get/<int:pk>/', views.get_post, name='get_post'),
    path('getPosts/', views.get_posts, name='get_posts'),
    path('getPost/<int:pk>/', views.get_post, name='get_post'),
    path('getUserPosts/<int:pk>/', views.get_user_posts, name="user-posts"),
    path('getpostscount/', views.get_posts_count, name="posts-count"),
    path('like/', views.put_like, name="like"),
    path('all/', views.get_all_post_poll, name="all-posts"),
    path('pdf/', views.create_pdf_post, name="pdf"),
    path('notification/', views.get_notifications, name="notification"),
]
