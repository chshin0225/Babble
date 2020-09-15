from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser

from babies.models import Baby

class User(AbstractUser):
    profile_image = models.CharField(max_length=200) 

    visited_babies = models.ManyToManyField(Baby, through='BabyAccess', related_name='visited_users')
    # ranks = models.ManyToManyField(Rank, through='UserBabyRelationship', related_name='rank_members')
    # groups = models.ManyToManyField(Group, through='UserBabyRelationship', related_name='group_participants')
    # babies = models.ManyToManyField(Baby, through='UserBabyRelationship', related_name='invited_users')


class BabyAccess(models.Model):
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    baby_id = models.ForeignKey(Baby, on_delete=models.CASCADE)
    last_access_date = models.DateField(auto_now=True)


class Rank(models.Model):
    rank_name = models.CharField(max_length=50)


class Group(models.Model):
    baby_id = models.ForeignKey(Baby, on_delete=models.CASCADE)
    group_name = models.CharField(max_length=50)
    

# class UserBabyRelationship(models.Model):
#     user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#     baby_id = models.ForeignKey(Baby, on_delete=models.CASCADE)
#     # 클래스가 지워진다면?
#     rank_id = models.ForeignKey(rank, on_delete=models.CASCADE)
#     # default값은 무소속?
#     group_id = models.ForeignKey(Group, on_delete=models.SET_DEFAULT, default=1)
#     relationship_name = models.CharField(max_length=50)
#     # creator_id =
#     # create_date =
#     # modifier_id = 
#     # modify_date = 