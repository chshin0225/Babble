from django.shortcuts import render, get_object_or_404

from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import PhotoListSerializer, PhotoDetailSerializer

from .models import Photo
# Create your views here.

class PhotoListView(APIView):
    # 아기의 전체 사진 조회
    def get(self, request):
        cb = request.user.current_baby
        if not cb:
            raise ValueError('아이를 생성하거나 선택해주세요.')
        photos = Photo.objects.filter(baby=cb)
        serializer = PhotoListSerializer(photos, many=True)
        return Response(serializer.data)

    # 아기 사진 업로드
    def post(self, request):
        cb = request.user.current_baby.id
        if not cb:
            raise ValueError('아이를 생성하거나 선택해주세요.')

        new_photos = request.data
        for photo in new_photos:
            photo["baby"] = cb
            serializer = PhotoDetailSerializer(data=photo)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
        return Response({"message":"사진이 등록되었습니다."})

class PhotoDetailView(APIView):
    def get(self, request, photo_id):
        photo = get_object_or_404(Photo, id=photo_id)
        serializer = PhotoDetailSerializer(photo)
        return Response(serializer.data)

    def put(self, request):
        pass

    def delete(self, request):
        pass
