from django.contrib import admin
from .models import Post, Comment, Like,UserDetails
from mptt.admin import MPTTModelAdmin

admin.site.register(Post)
admin.site.register(Comment, MPTTModelAdmin)
admin.site.register(Like)
admin.site.register(UserDetails)
