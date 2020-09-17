from django.shortcuts import render, get_object_or_404
from django.contrib.auth import get_user_model

from rest_framework.response import Response 
from rest_framework.views import APIView

from .serializers import DiaryListSerializer, DiarySerializer, DiaryCommentSerializer
from .models import Diary, DiaryComment
from babies.models import Baby

# Create your views here.
class DiaryListView(APIView):
    def get(self, request):
        # baby_id = request.user.current_baby
        baby_id = 1
        diaries = Diary.objects.filter(baby=baby_id)
        serializer = DiaryListSerializer(diaries, many=True)
        return Response(serializer.data)

    def post(self, request):
        # baby_id = request.user.current_baby
        baby_id = 1
        baby = get_object_or_404(Baby, id=baby_id)
        serializer = DiarySerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            # 유저 정보 필요!!
            User = get_user_model()
            admin = User.objects.get(id=1)
            serializer.save(creator=admin, baby=baby)
            # serializer.save(creator=request.user, baby=baby)
            return Response(serializer.data)
        return Response(serializer.errors)


class DiaryDetailView(APIView):
    def get(self, request, diary_id):
        diary = get_object_or_404(Diary, id=diary_id)
        serializer = DiarySerializer(diary)
        return Response(serializer.data)

    def put(self, request, diary_id):
        baby_id = request.user.current_baby
        baby = get_object_or_404(Baby, id=baby_id)
        diary = get_object_or_404(Diary, id=diary_id)
        serializer = DiarySerializer(diary, data=request.data)
        if serializer.is_valid(raise_exception=True):
            # creator? modifier? 둘 다?
            serializer.save(modifier=request.user, baby=baby)
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, diary_id):
        diary = get_object_or_404(Diary, id=diary_id)
        if diary.creator == request.user:
            diary.delete()
            return Response()
        return Response()

    
class DiaryCommentListView(APIView):
    def get(self, request, diary_id):
        diary = get_object_or_404(Diary, id=diary_id)
        serializer = DiaryCommentSerializer(diary.comments, many=True)
        return Response(serializer.data)

    def post(self, request, diary_id):
        diary = get_object_or_404(Diary, id=diary_id)
        serializer = DiaryCommentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user, diary=diary)
            return Response(serializer.data)
        return Response(serializer.errors)
        


class DiaryCommentDetailView(APIView):
    def put(self, request, diary_id, comment_id):
        diary = get_object_or_404(Diary, id=diary_id)
        comment = get_object_or_404(DiaryComment, id=comment_id)
        serializer = DiaryCommentSerializer(comment, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user, diary=diary)
            return Response(serializer.data)
        return Response(serializer.errors)
        

    def delete(self, request, diary_id, comment_id):
        comment = get_object_or_404(DiaryComment, id=comment_id)
        if comment.user == request.user:
            comment.delete()
            return Response()
        return Response(serializer.errors)