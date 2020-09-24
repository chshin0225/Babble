from rest_framework import serializers

from .models import Diary, DiaryComment
from accounts.models import UserBabyRelationship

from accounts.serializers import UserSerializer
from babies.serializers import BabySerializer

class DiaryListSerializer(serializers.ModelSerializer):
    # baby = BabySerializer(required=False)
    creator = UserSerializer(required=False)
    # modifier = UserSerializer(required=False)
    relationship_name = serializers.SerializerMethodField('get_relationship_name')
    class Meta:
        model = Diary
        fields = '__all__'

    def get_relationship_name(self, diary):
        relationship_name = UserBabyRelationship.objects.get(baby=diary.baby, user=diary.creator).relationship_name
        return relationship_name

class DiarySerializer(serializers.ModelSerializer):
    # baby = BabySerializer(required=False)
    creator = UserSerializer(required=False)
    # modifier = UserSerializer(required=False)
    class Meta:
        model = Diary
        fields = '__all__'

class DiaryCommentSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=False)
    # diary = DiarySerializer(required=False)
    relationship_name = serializers.SerializerMethodField('get_relationship_name')
    class Meta:
        model = DiaryComment
        fields = '__all__'

    def get_relationship_name(self, diarycomment):
        relationship_name = UserBabyRelationship.objects.get(baby=diarycomment.user.current_baby, user=diarycomment.user).relationship_name
        return relationship_name