from rest_framework import serializers
from .models import Diary, DiaryComment
from accounts.serializers import UserSerializer
from babies.serializers import BabySerializer

class DiaryListSerializer(serializers.ModelSerializer):
    # baby = BabySerializer(required=False)
    # creator = UserSerializer(required=False)
    # modifier = UserSerializer(required=False)
    class Meta:
        model = Diary
        fields = ['baby', 'title', 'content', 'creator', 'create_date', 'modifier', 'modify_date']

class DiarySerializer(serializers.ModelSerializer):
    # baby = BabySerializer(required=False)
    # creator = UserSerializer(required=False)
    # modifier = UserSerializer(required=False)
    class Meta:
        model = Diary
        fields = '__all__'

class DiaryCommentListSerializer(serializers.ModelSerializer):
    # user = UserSerializer(required=False)
    # diary = DiarySerializer(required=False)
    class Meta:
        model = DiaryComment
        fields = '__all__'