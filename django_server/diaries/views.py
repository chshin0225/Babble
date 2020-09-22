from django.shortcuts import render, get_object_or_404
from django.contrib.auth import get_user_model

from rest_framework.response import Response 
from rest_framework.views import APIView
from rest_framework import status

from .serializers import DiaryListSerializer, DiarySerializer, DiaryCommentSerializer
from accounts.serializers import SimpleUserBabyRelationshipSerializer

from .models import Diary, DiaryComment
from babies.models import Baby
from accounts.models import UserBabyRelationship

# Create your views here.
class DiaryListView(APIView):
    def get(self, request):
        baby_id = request.user.current_baby
        # baby_id = 1
        diaries = Diary.objects.filter(baby=baby_id)
        serializer = DiaryListSerializer(diaries, many=True)
        return Response(serializer.data)

    def post(self, request):
        baby_id = request.user.current_baby.id
        # baby_id = 1
        baby = get_object_or_404(Baby, id=baby_id)
        serializer = DiarySerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            # 유저 정보 필요!!
            serializer.save(creator=request.user, baby=baby)
            return Response(serializer.data)
        return Response(serializer.errors)


class DiaryDetailView(APIView):
    def get(self, request, diary_id):
        diary = get_object_or_404(Diary, id=diary_id)
        diary_serializer = DiarySerializer(diary)        

        # creator와 baby의 관계 정보 
        creator = diary.creator
        user_baby_relationship = UserBabyRelationship.objects.get(user=creator, baby=request.user.current_baby)
        user_baby_relationship_serializer = SimpleUserBabyRelationshipSerializer(user_baby_relationship)

        return Response({
            'diary': diary_serializer.data,
            'relationship': user_baby_relationship_serializer.data
        }, status=status.HTTP_200_OK)

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
        print(request.user)
        print(diary.creator)
        # if diary.creator == request.user:
        diary.delete()
        return Response()
        # return Response({'detail': '권한이 없습니다.'})

    
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