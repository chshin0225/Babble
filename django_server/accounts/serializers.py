from rest_framework import serializers

from .models import User, BabyAccess, Rank, Group, UserBabyRelationship
from babies.serializers import BabySerializer

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = []

class RankSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rank
        fields = '__all__'

class GroupListSerializer(serializers.ModelSerializer):
    baby = BabySerializer(required=False)
    class Meta:
        model = Group
        fields = '__all__'

class UserBabyRelationshipSerializer(serializers.ModelSerializer):
    baby = BabySerializer(required=False)
    rank = RankSerializer(required=False)
    class Meta:
        model = UserBabyRelationship
        fields = '__all__'