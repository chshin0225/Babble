from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model

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

    profile_image = models.CharField(max_length=200, blank=True, null=True)
    birth_height = models.FloatField()
    birth_weight = models.FloatField()
   

class BabyMeasurement(models.Model):
    baby = models.ForeignKey(Baby, blank=True, on_delete=models.CASCADE)
    weight = models.FloatField(blank=True, null=True)
    height = models.FloatField(blank=True, null=True)
    head_size = models.FloatField(blank=True, null=True)
    measure_date = models.DateField()
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True, on_delete=models.SET_NULL, related_name='created_measurements')
    create_date = models.DateTimeField(auto_now_add=True)
    modifier = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True, on_delete=models.SET_NULL, related_name='modified_measurements')
    modify_date = models.DateTimeField(auto_now=True)

