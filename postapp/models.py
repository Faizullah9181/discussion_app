from django.db import models
from user.models import Users
from pollapp.models import Poll


class Post(models.Model):
    title = models.CharField(null=False, blank=False, max_length=200)
    content = models.TextField(null=True, blank=True,max_length=2000)
    created_at = models.DateTimeField(null=True, blank=True)
    created_by = models.ForeignKey(Users, related_name='post_creator', on_delete=models.SET_NULL, null=True)
    last_modified_at = models.DateTimeField(null=True, blank=True, auto_now_add=True)
    last_modified_by = models.ForeignKey(Users, related_name='last_modifier', on_delete=models.SET_NULL, null=True)
    allow_comments = models.BooleanField(default=True)
    comment_count = models.IntegerField(blank=True, default=0)
    like_count = models.IntegerField(blank=True, default=0)
    post_image = models.CharField(max_length=255, blank=True)
    views = models.IntegerField(blank=True, default=0)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.title


class Comment(models.Model):
    content = models.TextField(null=True, blank=True, max_length=2000)
    created_at = models.DateTimeField(null=True, blank=True)
    created_by = models.ForeignKey(Users, related_name='comment_creator', on_delete=models.SET_NULL, null=True)
    last_modified_at = models.DateTimeField(null=True, blank=True, auto_now_add=True)
    post = models.ForeignKey(Post, related_name='post', on_delete=models.CASCADE, null=True)
    poll = models.ForeignKey(Poll, related_name='poll', on_delete=models.CASCADE, null=True)
    like_count = models.IntegerField(blank=True, default=0)
    reply_count = models.IntegerField(blank=True, default=0)

class Reply(models.Model):
    content = models.TextField(null=True, blank=True, max_length=2000)
    created_at = models.DateTimeField(null=True, blank=True)
    created_by = models.ForeignKey(Users, related_name='reply_creator', on_delete=models.SET_NULL, null=True)
    last_modified_at = models.DateTimeField(null=True, blank=True, auto_now_add=True)
    comment = models.ForeignKey(Comment, related_name='comment', on_delete=models.CASCADE, null=True)
    like_count = models.IntegerField(blank=True, default=0)


class Like(models.Model):
    post = models.ForeignKey(Post, related_name='post_likes', on_delete=models.DO_NOTHING, null=True, blank=True)
    poll = models.ForeignKey(Poll, related_name='poll_likes', on_delete=models.DO_NOTHING, null=True, blank=True)
    comment = models.ForeignKey(Comment, related_name='comment_likes', on_delete=models.CASCADE, null=True, blank=True)
    user = models.ForeignKey(Users, on_delete=models.SET_NULL, null=True)



class UserDetails(models.Model):
    user  = models.ForeignKey(Users, on_delete=models.CASCADE, null=True)
    username = models.CharField(null=False, blank=False, max_length=200)
    first_name = models.CharField(null=False, blank=False, max_length=200)
    last_name = models.CharField(null=False, blank=False, max_length=200)
    user_image = models.CharField(max_length=255, blank=True)
    user_post_count = models.IntegerField(blank=True, default=0 , null=True)
    user_poll_count = models.IntegerField(blank=True, default=0 , null=True)
    user_posts = models.ManyToManyField(Post, related_name='user_posts', blank=True)
    user_polls = models.ManyToManyField(Poll, related_name='user_polls', blank=True)

    def __str__(self):
        return self.username

    class Meta:
        ordering = ["-username"]