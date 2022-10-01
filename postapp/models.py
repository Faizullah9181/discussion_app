from django.db import models
from user.models import Users
from pollapp.models import Poll
from mptt.models import MPTTModel, TreeForeignKey


class Post(models.Model):
    title = models.CharField(null=False, blank=False, max_length=200)
    content = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(null=True, blank=True)
    created_by = models.ForeignKey(Users, related_name='post_creator', on_delete=models.SET_NULL, null=True)
    last_modified_at = models.DateTimeField(null=True, blank=True, auto_now_add=True)
    last_modified_by = models.ForeignKey(Users, related_name='last_modifier', on_delete=models.SET_NULL, null=True)
    allow_comments = models.BooleanField(default=True)
    comment_count = models.IntegerField(blank=True, default=0)
    like_count = models.IntegerField(blank=True, default=0)
    views = models.IntegerField(blank=True, default=0)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.title


class Comment(MPTTModel):
    post = models.ForeignKey(Post, related_name='post_comments', on_delete=models.DO_NOTHING, null=True, blank=True)
    poll = models.ForeignKey(Poll, related_name='poll_comments', on_delete=models.DO_NOTHING, null=True, blank=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    content = models.TextField(null=False, blank=False)
    like_count = models.IntegerField(blank=True, default=0)
    created_at = models.DateTimeField(null=True, blank=True, auto_now_add=True)
    created_by = models.ForeignKey(Users, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.content

    class MPTTMeta:
        order_insertion_by = ['created_at']


class Like(models.Model):
    post = models.ForeignKey(Post, related_name='post_likes', on_delete=models.DO_NOTHING, null=True, blank=True)
    poll = models.ForeignKey(Poll, related_name='poll_likes', on_delete=models.DO_NOTHING, null=True, blank=True)
    comment = models.ForeignKey(Comment, related_name='comment_likes', on_delete=models.CASCADE, null=True, blank=True)
    user = models.ForeignKey(Users, on_delete=models.SET_NULL, null=True)