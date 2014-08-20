from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.
class Post(models.Model):
    owner = models.ForeignKey('User')
    up_votes = models.IntegerField()
    down_votes = models.IntegerField()
    post_date = models.DateTimeField(auto_now_add = True)


class User(AbstractUser):
    profile_picture = models.ImageField("Image", upload_to="images/")
    # gender choice
    MALE = 'M'
    FEMALE = 'F'
    gender_choices = (
        (MALE, 'Male'),
        (FEMALE, 'Female'),
    )
    gender = models.CharField(max_length=1,
                              choices=gender_choices)

    birth_day = models.DateField(null=True)

    def __str__(self):
        return self.username

class Image(models.Model):
    post = models.OneToOneField(Post, primary_key=True)
    image = models.ImageField("Image", upload_to="images/")
    file_size = models.IntegerField()
    file_type = models.CharField(max_length=100)
    flags = models.ForeignKey('Report')

class Comment(models.Model):
    post = models.ForeignKey(Post)
    body = models.TextField(max_length=500)
    publish_date = models.DateTimeField(auto_now_add = True)
    is_spam = models.BooleanField()
    is_offensive = models.BooleanField()

class Report(models.Model):
    comment = models.ForeignKey(Comment)
    flagger = models.ForeignKey(User)
    flag_date = models.DateTimeField(auto_now_add = True)
    reason = models.CharField(max_length=500)
