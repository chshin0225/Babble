from django.db import models
from django.conf import settings

from accounts.models import Group
# from accounts.models import Group, UserBabyRelationship
from babies.models import Baby
from photos.models import Photo

# Create your models here.
class Diary(models.Model):
    baby_id = models.ForeignKey(Baby, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()
    content_html = models.TextField()
    
    # 최고권위자 class의 class_id가 1이라는 가정 하에
    # owner_id = UserBabyRelationship.objects.get(baby_id=baby_id, class_id=1).values('user_id')
    owner_id = 1
    creator_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_DEFAULT, default=owner_id, related_name='created_diaries')
    create_date = models.DateField(auto_now_add=True)
    modifier_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_DEFAULT, default=owner_id, related_name='modified_diaries')
    modify_date = models.DateField(auto_now=True)

    permitted_groups = models.ManyToManyField(Group, related_name='allowed_diaries')
    featured_photos = models.ManyToManyField(Photo, related_name='related_diaries')


class DiaryComment(models.Model):
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    diary_id = models.ForeignKey(Diary, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateField(auto_now_add=True)
    modify_date = models.DateField(auto_now=True)