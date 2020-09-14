from django.db import models
from django.conf import settings

# Create your models here.
class Photo(models.Model):
    # Baby 모델 가져오기
    baby_id = models.ForeignKey('Baby', on_delete=models.CASCADE)
    image_url = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    # 사진 올린 사람의 user_id?
    create_id = 
    # 사진의 metadata 뽑아오는법?
    created_date = models.DatetField()
    # 사진 수정한 사람의 user_id?
    modify_id = 
    modify_date = models.DateField(auto_now=True)

class Album(models.Model):
    # Baby 모델 가져오기
    baby_id = models.ForeignKey('Baby', on_delete=models.CASCADE)
    album_name = models.CharField(max_length=50)
    # on_delete 옵션?
    create_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=)
    create_date = models.DateField(auto_now_add=True)
    # on_delete 옵션?
    modify_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=)
    modify_date = models.DateField(auto_now=True)
    photos = models.ManyToManyField('Photo', related_name='albums')