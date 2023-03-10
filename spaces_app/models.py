from django.db import models
from postapp.models import *
from user.models import *
from pollapp.models import *


# Create your models here.

class spaces(models.Model):
    space_name = models.CharField(null=False, blank=False, max_length=200)
    space_description = models.TextField(null=True, blank=True,max_length=2000)
    space_image = models.URLField(null=True, blank=True,max_length=2000)
    space_created_at = models.DateTimeField(null=True, blank=True)
    space_created_by = models.ForeignKey(Users, related_name='space_creator', on_delete=models.SET_NULL, null=True)
    space_last_modified_at = models.DateTimeField(null=True, blank=True, auto_now_add=True)
    space_last_modified_by = models.ForeignKey(Users, related_name='space_last_modifier', on_delete=models.SET_NULL, null=True)
    space_post_count = models.IntegerField(blank=True, default=0 , null=True)
    space_poll_count = models.IntegerField(blank=True, default=0 , null=True)
    space_posts = models.ManyToManyField(Post, related_name='space_posts', blank=True)
    space_polls = models.ManyToManyField(Poll, related_name='space_polls', blank=True)
    space_members = models.ManyToManyField(Users, related_name='space_members', blank=True)
    space_admins = models.ManyToManyField(Users, related_name='space_admins', blank=True)

    class Meta:
        ordering = ["-space_created_at"]

    def __str__(self):
        return self.space_name
