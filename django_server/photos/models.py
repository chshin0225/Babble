from django.db import models
from django.conf import settings

from accounts.models import Group
# from accounts.models import Group, UserBabyRelationship
from babies.models import Baby

# Create your models here.
class Tag(models.Model):
    tag_name = models.CharField(max_length=50)

class Photo(models.Model):
    baby_id = models.ForeignKey(Baby, on_delete=models.CASCADE)
    image_url = models.CharField(max_length=200)
    location = models.CharField(max_length=200)

    # 최고권위자 class의 class_id가 1이라는 가정 하에
    # owner_id = UserBabyRelationship.objects.get(baby_id=baby_id, class_id=1).values('user_id')
    owner_id = 1
    creator_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_DEFAULT, default=owner_id, related_name='created_photos')
    # 사진의 metadata?
    create_date = models.DateField(auto_now_add=True)
    modifier_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_DEFAULT, default=owner_id, related_name='modified_photos')
    modify_date = models.DateField(auto_now=True)

    permitted_groups = models.ManyToManyField(Group, related_name='allowed_photos')
    photo_tags = models.ManyToManyField(Tag, related_name='tagged_photos')


class PhotoComment(models.Model):
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    photo_id = models.ForeignKey(Photo, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateField(auto_now_add=True)
    modify_date = models.DateField(auto_now=True)


class Album(models.Model):
    baby_id = models.ForeignKey(Baby, on_delete=models.CASCADE)
    album_name = models.CharField(max_length=50)

    # 최고권위자의 class_id가 1이라는 가정 하에
    # owner_id = UserBabyRelationship.objects.get(baby_id=baby_id, class_id=1).values('user_id')
    owner_id = 1
    creator_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_DEFAULT, default=owner_id, related_name='created_albums')
    create_date = models.DateField(auto_now_add=True)
    modifier_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_DEFAULT, default=owner_id, related_name='modified_albums')
    modify_date = models.DateField(auto_now=True)

    photos = models.ManyToManyField(Photo, related_name='albums')
    album_tags = models.ManyToManyField(Tag, related_name='tagged_albums')


