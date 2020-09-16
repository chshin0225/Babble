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
    baby = models.ForeignKey(Baby, on_delete=models.CASCADE)
    weight = models.FloatField()
    height = models.FloatField()
    measure_date = models.DateField()

    # 최고권위자 class의 class_id가 1이라는 가정 하에
    # owner = UserBabyRelationship.objects.get(baby=baby, class=1)
    owner = 1
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_DEFAULT, default=owner, related_name='created_measurements')
    create_date = models.DateField(auto_now_add=True)
    modifier = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_DEFAULT, default=owner, related_name='modified_measurements')
    modify_date = models.DateField(auto_now=True)