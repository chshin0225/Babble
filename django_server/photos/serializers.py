from rest_framework import serializers
from .models import Tag, Photo, PhotoComment, Album
from accounts.serializers import GroupListSerializer
class TagListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'

class PhotoListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = ['id', 'image_url']

class PhotoDetailSerializer(serializers.ModelSerializer):
    permitted_groups = GroupListSerializer(required=False, many=True)
    photo_tags = TagListSerializer(required=False, many=True)
    class Meta:
        model = Photo
        fields = '__all__'