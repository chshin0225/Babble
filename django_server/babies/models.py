from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model

# from accounts.models import UserBabyRelationship

# Create your models here.
class Baby(models.Model):
    baby_name = models.CharField(max_length=50)
    birth = models.DateField()

    GENDER_CHOICES = [
        ('F', 'Female'),
        ('M', 'Male'),
    ]
    gender = models.CharField(
        max_length=1,
        choices=GENDER_CHOICES,
        default='F',
    )

    profile_image = models.CharField(max_length=200)
    birth_height = models.FloatField()
    birth_weight = models.FloatField()
   

class BabyMeasurement(models.Model):
    baby_id = models.ForeignKey(Baby, on_delete=models.CASCADE)
    weight = models.FloatField()
    height = models.FloatField()
    measure_date = models.DateField()

    # 최고권위자 class의 class_id가 1이라는 가정 하에
    # owner_id = UserBabyRelationship.objects.get(baby_id=baby_id, class_id=1).values('user_id')
    owner_id = 1
    creator_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_DEFAULT, default=owner_id, related_name='created_measurements')
    create_date = models.DateField(auto_now_add=True)
    modifier_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_DEFAULT, default=owner_id, related_name='modified_measurements')
    modify_date = models.DateField(auto_now=True)