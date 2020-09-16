from rest_framework import serializers

from .models import User, BabyAccess, Rank, Group, UserBabyRelationship
from babies.serializers import BabySerializer

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class GroupListSerializer(serializers.ModelSerializer):
    baby = BabySerializer(required=False)
    class Meta:
        model = Group
        fields = '__all__'