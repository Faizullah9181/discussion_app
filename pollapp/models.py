from django.db import models
from user.models import Users


class Poll(models.Model):
    title = models.CharField(null=False, blank=False, max_length=200)
    content = models.TextField(null=False, blank=False)
    created_at = models.DateTimeField(null=True, blank=True)
    created_by = models.ForeignKey(Users, related_name='creator', on_delete=models.SET_NULL, null=True)
    last_modified_at = models.DateTimeField(null=True, blank=True, auto_now_add=True)
    last_modified_by = models.ForeignKey(Users, related_name='modifier', on_delete=models.SET_NULL, null=True)
    private= models.BooleanField(default=False)
    allow_comments = models.BooleanField(default=True)
    comment_count = models.IntegerField(blank=True, default=0)
    total_votes = models.IntegerField(blank=True, default=0, null=True)
    is_voted = models.BooleanField(default=False)
    is_liked = models.BooleanField(default=False)
    liked_by = models.ManyToManyField(Users, related_name='liked_by_poll')
    poll_option = models.JSONField(null=True, blank=True)
    like_count = models.IntegerField(blank=True, default=0)
    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.title


class PollOption(models.Model):
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
    content = models.TextField(null=True, blank=True,max_length=2000)
    votes = models.IntegerField(blank=True, default=0)
    voted_by = models.ManyToManyField(Users, related_name='voted_by')

    