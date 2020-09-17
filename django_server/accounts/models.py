from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser, BaseUserManager

from babies.models import Baby

class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)
    
    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser mush have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser mush have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)

class User(AbstractUser):
    first_name = None
    last_name = None
    username = None
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)

    name = models.CharField(blank=True, max_length=50)
    profile_image = models.CharField(max_length=200) 
    visited_babies = models.ManyToManyField(Baby, through='BabyAccess', related_name='visited_users')
    
    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

class BabyAccess(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    baby = models.ForeignKey(Baby, on_delete=models.CASCADE)
    last_access_date = models.DateField(auto_now=True)


class Rank(models.Model):
    rank_name = models.CharField(max_length=50)


class Group(models.Model):
    baby = models.ForeignKey(Baby, on_delete=models.CASCADE)
    group_name = models.CharField(max_length=50)
    

class UserBabyRelationship(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    baby = models.ForeignKey(Baby, on_delete=models.CASCADE)
    # 클래스가 지워진다면?
    rank = models.ForeignKey(Rank, on_delete=models.CASCADE)
    # default값은 무소속?
    group = models.ForeignKey(Group, blank=True, null=True, on_delete=models.SET_NULL)
    relationship_name = models.CharField(max_length=50)