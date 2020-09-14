from django.db import models
from django.conf import settings

# Create your models here.
class Diary(models.Model):
    # Baby 모델 가져오기
    baby_id = models.ForeignKey('Baby', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()
    content_html = models.TextField()
    # on_delete 옵션?
    create_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=)
    create_date = models.DateField(auto_now_add=True)
    # on_delete 옵션?
    modify_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=)
    modify_date = models.DateField(auto_now=True)