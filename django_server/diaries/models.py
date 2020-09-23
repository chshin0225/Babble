from django.db import models
from django.conf import settings

from accounts.models import Group
# from accounts.models import Group, UserBabyRelationship
from babies.models import Baby
from photos.models import Photo

# Create your models here.
class Diary(models.Model):
    baby = models.ForeignKey(Baby, blank=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()
    content_html = models.TextField()
    diary_date = models.DateField()

    # owner = UserBabyRelationship.objects.get(baby=baby, class=1)
    owner = 1
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_DEFAULT, default=owner, related_name='created_diaries')
    create_date = models.DateTimeField(auto_now_add=True)
    modifier = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True, on_delete=models.SET_NULL, related_name='modified_diaries')
    modify_date = models.DateTimeField(auto_now=True)
    cover_photo = models.CharField(max_length=200, blank=True, null=True)

    permitted_groups = models.ManyToManyField(Group, blank=True, related_name='allowed_diaries')
    featured_photos = models.ManyToManyField(Photo, blank=True, related_name='related_diaries')


class DiaryComment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, on_delete=models.CASCADE, related_name='diary_comments')
    diary = models.ForeignKey(Diary, blank=True, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    create_date = models.DateTimeField(auto_now_add=True)
    modify_date = models.DateTimeField(auto_now=True)
    