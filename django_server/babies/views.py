from django.shortcuts import render, get_object_or_404

from rest_framework.response import Response
from rest_framework.views import APIView
# from rest_framework.permissions import IsAuthenticated

from .serializers import BabyListSerializer, BabySerializer, BabyMeasurementSerializer
from accounts.serializers import UserBabyRelationshipSerializer, BabyAccessSerializer

from .models import Baby
from accounts.models import User, UserBabyRelationship, Rank

# Create your views here.
class BabyListView(APIView):
    # permission_classes = ['IsAuthenticated']
    def get(self, request):
        my_babies = UserBabyRelationship.objects.filter(user=request.user).all()
        serializer = UserBabyRelationshipSerializer(my_babies, many=True)
        return Response(serializer.data)

    # 새로운 babble box 생성
    def post(self, request):
        baby_serializer = BabySerializer(data=request.data['baby'])
        if baby_serializer.is_valid(raise_exception=True):
            baby_serializer.save()
            # user_baby_relationship 만들기 
            baby_id = baby_serializer.data['id']
            baby = Baby.objects.get(id=baby_id)
            owner = Rank.objects.get(id=1)
            user_id = User.objects.get(email=request.user).id
            user_baby_relationship = {
                'user': user_id,
                'relationship_name': request.data['relationship_name']
            }
            relationship_serializer = UserBabyRelationshipSerializer(data=user_baby_relationship)
            if relationship_serializer.is_valid(raise_exception=True):
                relationship_serializer.save(baby=baby, rank=owner)

                # 유저 데이터의 current_baby 업데이트
                user = request.user
                user.current_baby = baby
                user.save()

                # BabyAccess에 방문 기록 추가 
                baby_access_data = {
                    "baby": baby_id,
                    "user": user_id
                }
                baby_access_serializer = BabyAccessSerializer(data=baby_access_data)
                if baby_access_serializer.is_valid(raise_exception=True):
                    baby_access_serializer.save()
                    return Response(relationship_serializer.data)
                return Response(baby_access_data.errors)
            return Response(relationship_serializer.errors)
        return Response(serializer.errors)


class BabyDetailView(APIView):
    # 해당 babble box 회원들만 조회 가능
    def get(self, request, baby_id):
        members = UserBabyRelationship.objects.filter(baby=baby_id).values_list('user', flat=True)
        user_id = User.objects.get(email=request.user).id
        if user_id in members:
            baby = Baby.objects.get(id=baby_id)
            serializer = BabySerializer(baby)
            return Response(serializer.data)
        return Response({'detail': '권한이 없습니다.'})

    # 해당 babble box 생성자만 수정 가능
    def put(self, request, baby_id):
        owner = UserBabyRelationship.objects.get(baby=baby_id, rank=1).user
        if owner == request.user:
            baby = Baby.objects.get(id=baby_id)
            serializer = BabySerializer(baby, data=request.data)
            if serializer.is_valid():
                serializer.save()
            return Response(serializer.errors)
        return Response({'detail': '권한이 없습니다.'})

    # 해당 babble box 생성자만 삭제 가능
    def delete(self, request, baby_id):
        owner = UserBabyRelationship.objects.get(baby=baby_id, rank=1).user
        baby = Baby.objects.get(id=baby_id)
        if owner == request.user:
            baby.delete()
            return Response()
        return Response({'detail': '권한이 없습니다.'})


class UserBabyRelationshipListView(APIView):
    def get(self, request):
        user_id = User.objects.get(email=request.user).id
        user_baby_relationships = UserBabyRelationship.objects.filter(user=user_id).all()
        serializer = UserBabyRelationshipSerializer(user_baby_relationships, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = UserBabyRelationshipSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)