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
    is_liked = models.BooleanField(default=False)
    Liked_by = models.ManyToManyField(Users, related_name='liked_by_post')
    comment_count = models.IntegerField(blank=True, default=0)
    like_count = models.IntegerField(blank=True, default=0)
    post_image = models.CharField(max_length=255, blank=True, null=True)
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
    parent_id = models.ForeignKey('self', related_name='childrens', on_delete=models.CASCADE, null=True, blank=True)
    replies = models.ManyToManyField('self', related_name='parent', symmetrical=False, blank=True)
    Liked_by = models.ManyToManyField(Users, related_name='liked_by_comment')
    is_liked = models.BooleanField(default=False)

class Like(models.Model):
    post = models.ForeignKey(Post, related_name='post_likes', on_delete=models.SET_NULL, null=True, blank=True)
    poll = models.ForeignKey(Poll, related_name='poll_likes', on_delete=models.SET_NULL, null=True, blank=True)
    comment = models.ForeignKey(Comment, related_name='comment_likes', on_delete=models.CASCADE, null=True, blank=True)
    user = models.ForeignKey(Users, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(null=True, blank=True)
    created_by = models.ForeignKey(Users, related_name='like_creator', on_delete=models.SET_NULL, null=True)


class UserDetails(models.Model):
    user  = models.ForeignKey(Users, on_delete=models.CASCADE, null=True)
    username = models.CharField(null=False, blank=False, max_length=200)
    first_name = models.CharField(null=False, blank=False, max_length=200)
    last_name = models.CharField(null=False, blank=False, max_length=200)
    user_image = models.URLField(null=True, blank=True,max_length=2000)
    user_post_count = models.IntegerField(blank=True, default=0 , null=True)
    user_poll_count = models.IntegerField(blank=True, default=0 , null=True)
    user_posts = models.ManyToManyField(Post, related_name='user_posts', blank=True)
    user_polls = models.ManyToManyField(Poll, related_name='user_polls', blank=True)

    def __str__(self):
        return self.username

    class Meta:
        ordering = ["-username"]


class Notifications(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE, null=True)
    type = models.CharField(null=False, blank=False, max_length=200)
    post = models.ForeignKey(Post, related_name='post_notification', on_delete=models.CASCADE, null=True, blank=True)
    poll = models.ForeignKey(Poll, related_name='poll_notification', on_delete=models.CASCADE, null=True, blank=True)
    comment = models.ForeignKey(Comment, related_name='comment_notification', on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(null=True, blank=True)
    created_by = models.ForeignKey(Users, related_name='notification_creator', on_delete=models.SET_NULL, null=True)
    is_read = models.BooleanField(default=False)
    users = models.ManyToManyField(Users, related_name='users', blank=True)

    

    class Meta:
        ordering = ["-created_at"]



# from faker import Faker               
# from postapp.models import Post
# from user.models import Users
# faker = Faker()




# for i in range(50):
#        user = Users.objects.filter(id=1).first()
#        post=Post()
#        post.title=faker.sentence()
#        post.content=faker.text()
#        post.created_at="2022-11-18T15:16:38.685406Z"
#        post.created_by=  user
#        post.last_modified_at="2022-11-18T15:16:38.685406Z"
#        post.last_modified_by= user
#        post.allow_comments=True
#        post.comment_count=0
#        post.like_count = 0
#        post.post_image = faker.image_url()
#        post.views=0
#        post.save()