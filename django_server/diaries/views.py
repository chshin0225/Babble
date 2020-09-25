from django.shortcuts import render, get_object_or_404
from django.contrib.auth import get_user_model
from django.db.models import Q

from rest_framework.response import Response 
from rest_framework.views import APIView
from rest_framework import status

from .serializers import DiaryListSerializer, DiarySerializer, DiaryCommentSerializer
from accounts.serializers import SimpleUserBabyRelationshipSerializer
from babies.serializers import BabyMeasurementSerializer

from .models import Diary, DiaryComment
from babies.models import Baby, BabyMeasurement
from accounts.models import UserBabyRelationship

# Create your views here.
class DiaryListView(APIView):
    def get(self, request):
        baby_id = request.user.current_baby
        diaries = Diary.objects.filter(baby=baby_id).order_by('-diary_date')
        serializer = DiaryListSerializer(diaries, many=True)
        return Response(serializer.data)

    def post(self, request):
        baby_id = request.user.current_baby.id
        baby = get_object_or_404(Baby, id=baby_id)
        serializer = DiarySerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(creator=request.user, baby=baby)
            return Response(serializer.data)
        return Response(serializer.errors)


class DiaryPhotoListView(APIView):
    def get(self, request):
        baby_id = request.user.current_baby
        photo_diaries = Diary.objects.filter( cover_photo__isnull=False, baby=baby_id).order_by('-diary_date')
        serializer = DiaryListSerializer(photo_diaries, many=True)
        return Response(serializer.data)


class DiaryDetailView(APIView):
    def get(self, request, diary_id):
        diary = get_object_or_404(Diary, id=diary_id)
        diary_serializer = DiarySerializer(diary)        

        # creator와 baby의 관계 정보 
        creator = diary.creator
        user_baby_relationship = UserBabyRelationship.objects.get(user=creator, baby=request.user.current_baby)
        user_baby_relationship_serializer = SimpleUserBabyRelationshipSerializer(user_baby_relationship)

        # 해당 날짜에 기록한 성장 기록이 있는지 확인 후 있으면 성장 기록도 리턴 
        if BabyMeasurement.objects.filter(measure_date=diary.diary_date).exists():
            measurement = BabyMeasurement.objects.get(measure_date=diary.diary_date)
            measurement_serializer = BabyMeasurementSerializer(measurement)
            return Response({
                'diary': diary_serializer.data,
                'relationship': user_baby_relationship_serializer.data,
                'measurement': measurement_serializer.data
            }, status=status.HTTP_200_OK)
        else:
            return Response({
                'diary': diary_serializer.data,
                'relationship': user_baby_relationship_serializer.data
            }, status=status.HTTP_200_OK)

    def put(self, request, diary_id):
        baby_id = request.user.current_baby.id
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
        serializer = DiaryCommentSerializer(diary.comments.order_by('-create_date'), many=True)
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
        return Response({"message": "작성자만 삭제할 수 있습니다."}, status=400)