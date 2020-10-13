from rest_framework import serializers

from .models import Tag, Photo, PhotoComment, Album
from accounts.models import UserBabyRelationship

from accounts.serializers import UserSerializer, GroupListSerializer

class TagListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'

class SimplePhotoListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = ['id']

class PhotoListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = ['id', 'image_url', 'last_modified', 'create_date', 'modify_date', 'permitted_groups']

class PhotoDetailSerializer(serializers.ModelSerializer):
    permitted_groups = GroupListSerializer(required=False, many=True)
    photo_tags = TagListSerializer(required=False, many=True)
    class Meta:
        model = Photo
        fields = '__all__'

class PhotoCommentSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=False)
    photo = PhotoListSerializer(required=False)
    relationship_name = serializers.SerializerMethodField('get_relationship_name')
    class Meta:
        model = PhotoComment
        fields = '__all__'

    def get_relationship_name(self, photocomment):
        relationship_name = UserBabyRelationship.objects.get(baby=photocomment.user.current_baby, user=photocomment.user).relationship_name
        return relationship_name


class AlbumListSerializer(serializers.ModelSerializer):
    album_tags = TagListSerializer(required=False, many=True)
    class Meta:
        model = Album
        fields = ['id', 'baby', 'album_name', 'cover_photo', 'album_tags']


class AlbumDetailSerializer(serializers.ModelSerializer):
    album_tags = TagListSerializer(required=False, many=True)
    photos = PhotoDetailSerializer(required=False, many=True)
    class Meta:
        model = Album
        fields = '__all__'