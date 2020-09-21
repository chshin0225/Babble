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
        photos = Photo.objects.filter(baby=cb).order_by('-last_modified')
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
                serializer.save(creator=request.user, modifier=request.user)
        return Response({"message":"사진이 등록되었습니다."})

class PhotoDetailView(APIView):
    # 특정 사진 디테일 정보 조회
    def get(self, request, photo_id):
        photo = get_object_or_404(Photo, id=photo_id)
        if request.user.current_baby == photo.baby:
            serializer = PhotoDetailSerializer(photo)
            return Response(serializer.data)
        else:
            raise ValueError('해당 사진을 가져올 수 없습니다.')
    
    # 특정 사진 디테일 정보 수정
    def put(self, request, photo_id):
        cb = request.user.current_baby.id
        if not cb:
            raise ValueError('아이를 생성하거나 선택해주세요.')
        photo = get_object_or_404(Photo, id=photo_id)
        request.data["baby"] = cb
        # 여기서 권한 검증이 한 번 들어가줘야함
        serializer = PhotoDetailSerializer(photo, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(modifier=request.user)
            return Response(serializer.data)
        return Response(serializer.errors)

    # 특정 사진 삭제
    def delete(self, request, photo_id):
        photo = get_object_or_404(Photo, id=photo_id)
        # 여기서 권한 검증이 한 번 들어가줘야함 
        photo.delete()
        return Response({"message":"사진이 삭제되었습니다."})
