from django.contrib import admin
from .models import Post, Comment, Like
from mptt.admin import MPTTModelAdmin

admin.site.register(Post)
admin.site.register(Comment, MPTTModelAdmin)
admin.site.register(Like)
