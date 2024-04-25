from django.db import models

class Users(models.Model):
    UID = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=100)
    mobile_no = models.CharField(max_length=15)
    email = models.EmailField(unique=True)


class SocialMedia(models.Model):
    uid = models.CharField(max_length=50)
    platform_name = models.CharField(max_length=100)
    username = models.CharField(max_length=100)

class Analytics(models.Model):
    UID = models.CharField(max_length=50)
    platform_name = models.CharField(max_length=100)
    total_followers = models.IntegerField()
    total_views = models.IntegerField()
    total_likes = models.IntegerField()
    total_comments = models.IntegerField()
    growth_rate = models.FloatField()
