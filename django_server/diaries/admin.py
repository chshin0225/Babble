from django.contrib import admin
from .models import Diary, DiaryComment, DiaryGroup

# Register your models here.
admin.site.register(Diary)
admin.site.register(DiaryComment)
admin.site.register(DiaryGroup)