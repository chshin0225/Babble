from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser, BaseUserManager

from babies.models import Baby

class UserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError(_('The Email must be set'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        self.cleaned_data = self.get_cleaned_data()
        user.name = self.cleaned_data.get('name')
        user.profile_image = self.cleaned_data.get('profile_image')

        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))

        if not email:
            raise ValueError(_('The Email must be set'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)

        user.save()
        return user

class User(AbstractUser):
    first_name = None
    last_name = None
    username = None
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    
    user_type = models.CharField(default='basic', max_length=50)
    name = models.CharField(blank=True, null=True, max_length=50)
    profile_image = models.CharField(blank=True, null=True, max_length=200)
    current_baby = models.ForeignKey(Baby, null=True, blank=True, on_delete=models.SET_NULL)
    visited_babies = models.ManyToManyField(Baby, through='BabyAccess', related_name='visited_users')
    
    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

class BabyAccess(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, on_delete=models.CASCADE)
    baby = models.ForeignKey(Baby, on_delete=models.CASCADE)
    last_access_date = models.DateTimeField(auto_now_add=True)


class Rank(models.Model):
    rank_name = models.CharField(max_length=50)


class Group(models.Model):
    baby = models.ForeignKey(Baby, blank=True, on_delete=models.CASCADE)
    group_name = models.CharField(max_length=50)
    

class UserBabyRelationship(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    baby = models.ForeignKey(Baby, blank=True, on_delete=models.CASCADE)
    # 클래스가 지워진다면?
    rank = models.ForeignKey(Rank, blank=True, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, blank=True, null=True, on_delete=models.SET_NULL)
    relationship_name = models.CharField(max_length=50)

class Invitation(models.Model):
    baby = models.ForeignKey(Baby, on_delete=models.CASCADE)
    rank = models.ForeignKey(Rank, on_delete=models.CASCADE)
    token = models.TextField(blank=True)
    closed = models.BooleanField(default=False)

