from django.db import models
from django.conf import settings

from accounts.models import Group
# from accounts.models import Group, UserBabyRelationship
from babies.models import Baby

# Create your models here.
class Tag(models.Model):
    tag_name = models.CharField(max_length=50)

class Photo(models.Model):
    baby = models.ForeignKey(Baby, on_delete=models.CASCADE)
    image_url = models.CharField(max_length=200)
    file_type = models.CharField(max_length=50)
    last_modified = models.DateTimeField()
    size = models.IntegerField()
    # location = models.CharField(max_length=200, blank=True, null=True)

    # 최고권위자 class의 class_id가 1이라는 가정 하에
    # owner = UserBabyRelationship.objects.get(baby=baby, class=1)
    owner = 1
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_DEFAULT, default=owner, related_name='created_photos')
    # 사진의 metadata?
    create_date = models.DateTimeField(auto_now_add=True)
    modifier = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True, on_delete=models.SET_DEFAULT, default=owner, related_name='modified_photos')
    modify_date = models.DateTimeField(auto_now=True)

    permitted_groups = models.ManyToManyField(Group, related_name='allowed_photos')
    photo_tags = models.ManyToManyField(Tag, related_name='tagged_photos', through='PhotoTag')

class PhotoTag(models.Model):
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    photo = models.ForeignKey(Photo, on_delete=models.CASCADE)

class PhotoComment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='photo_comments')
    photo = models.ForeignKey(Photo, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    create_date = models.DateTimeField(auto_now_add=True)
    modify_date = models.DateTimeField(auto_now=True)


class Album(models.Model):
    baby = models.ForeignKey(Baby, blank=True, on_delete=models.CASCADE)
    album_name = models.CharField(max_length=50)
    
    # 최고권위자 class의 class_id가 1이라는 가정 하에
    # owner = UserBabyRelationship.objects.get(baby=baby, class=1)
    owner = 1
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, on_delete=models.SET_DEFAULT, default=owner, related_name='created_albums')
    create_date = models.DateTimeField(auto_now_add=True)
    modifier = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True, on_delete=models.SET_DEFAULT, default=owner, related_name='modified_albums')
    modify_date = models.DateTimeField(auto_now=True)
    cover_photo = models.TextField(blank=True, null=True)

    photos = models.ManyToManyField(Photo, blank=True, related_name='albums', through='AlbumPhotoRelationship')
    album_tags = models.ManyToManyField(Tag, blank=True, related_name='tagged_albums', through='AlbumTag')

class AlbumPhotoRelationship(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    photo = models.ForeignKey(Photo, on_delete=models.CASCADE)

class AlbumTag(models.Model):
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)


