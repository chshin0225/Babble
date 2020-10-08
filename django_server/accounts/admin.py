from django.contrib import admin
from .models import User, BabyAccess, Rank, Group, UserBabyRelationship, Invitation

# Register your models here.
admin.site.register(User)
admin.site.register(BabyAccess)
admin.site.register(Rank)
admin.site.register(Group)
admin.site.register(UserBabyRelationship)
admin.site.register(Invitation)