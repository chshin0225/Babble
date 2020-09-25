from django.shortcuts import render, get_object_or_404

from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import TagListSerializer, PhotoListSerializer, PhotoDetailSerializer, PhotoCommentSerializer

from .models import Tag, Photo, PhotoComment, PhotoTag
# Create your views here.

class TagListView(APIView):
    def get(self, request):
        tags = Tag.objects.all()
        serializer = TagListSerializer(tags, many=True)
        return Response(serializer.data) 

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
                created_photo = serializer.save(creator=request.user, modifier=request.user)
            # tag
            for tag_name in photo['tags']:
                try:
                    tag = Tag.objects.get(tag_name=tag_name)
                except:
                    tag = Tag(tag_name=tag_name)
                    tag.save()
                PhotoTag(tag=tag, photo=created_photo).save()
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
            
            photo.photo_tags.clear()
            for tag_name in request.data['tags']:
                try:
                    tag = Tag.objects.get(tag_name=tag_name)
                except:
                    tag = Tag(tag_name=tag_name)
                    tag.save()
                PhotoTag(tag=tag, photo=photo).save()

            return Response(serializer.data)
        return Response(serializer.errors)

    # 특정 사진 삭제
    def delete(self, request, photo_id):
        photo = get_object_or_404(Photo, id=photo_id)
        # 여기서 권한 검증이 한 번 들어가줘야함 
        photo.delete()
        return Response({"message":"사진이 삭제되었습니다."})


class PhotoCommentListView(APIView):
    # 사진 댓글 리스트 조회
    def get(self, request, photo_id):
        photo = get_object_or_404(Photo, id=photo_id)
        serializer = PhotoCommentSerializer(photo.comments.order_by('-create_date'), many=True)
        return Response(serializer.data)

    # 사진 댓글 생성
    def post(self, request, photo_id):
        photo = get_object_or_404(Photo, id=photo_id)
        serializer = PhotoCommentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user, photo=photo)
        return Response(serializer.data)


class PhotoCommentDetailView(APIView):
    # 사진 댓글 수정
    def put(self, request, photo_id, comment_id):
        comment = get_object_or_404(PhotoComment, id=comment_id)
        # 여기서 권한 검증이 한 번 들어가줘야함
        if comment.user.id == request.user.id:
            serializer = PhotoCommentSerializer(comment, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors)
        else:
            return Response({"message": "작성자만 수정할 수 있습니다."}, status=400)

    # 사진 댓글 삭제
    def delete(self, request, photo_id, comment_id):
        comment = get_object_or_404(PhotoComment, id=comment_id)
        if comment.user.id == request.user.id:
            comment.delete()
            return Response({"message":"댓글이 삭제되었습니다."}, status=200)
        else:
            return Response({"message": "작성자만 삭제할 수 있습니다."}, status=400)


class PhotoSearchView(APIView):
    def post(self, request):
        keyword = request.data["keyword"]
        cb = request.user.current_baby.id
        if not cb:
            raise ValueError('아이를 생성하거나 선택해주세요.')
        searched_photos = Photo.objects.none()
        tags = Tag.objects.filter(tag_name__icontains=keyword)
        for tag in tags:
            searched_photos = searched_photos | tag.tagged_photos.all()
        searched_photos = searched_photos.filter(baby=cb)
        serializer = PhotoListSerializer(searched_photos, many=True)
        return Response(serializer.data)