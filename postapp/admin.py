from django.contrib import admin
from .models import Post, Comment, Like,UserDetails,Notifications

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Like)
admin.site.register(UserDetails)
admin.site.register(Notifications)
