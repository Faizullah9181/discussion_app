from django.db import models
from user.models import Users


class Poll(models.Model):
    title = models.CharField(null=False, blank=False, max_length=200)
    content = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(null=True, blank=True)
    created_by = models.ForeignKey(Users, related_name='creator', on_delete=models.SET_NULL, null=True)
    last_modified_at = models.DateTimeField(null=True, blank=True, auto_now_add=True)
    last_modified_by = models.ForeignKey(Users, related_name='modifier', on_delete=models.SET_NULL, null=True)
    allow_comments = models.BooleanField(default=True)
    comment_count = models.IntegerField(blank=True, default=0)
    like_count = models.IntegerField(blank=True, default=0)
    views = models.IntegerField(blank=True, default=0)
    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.title


class PollOption(models.Model):
    poll = models.ForeignKey(Poll, related_name='poll_options', on_delete=models.DO_NOTHING)
    option_detail = models.CharField(null=False, blank=False, max_length=400)
    votes = models.IntegerField(blank=True, default=0)
    voted=models.JSONField(default=dict)
