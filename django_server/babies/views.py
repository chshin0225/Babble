from django.shortcuts import render, get_object_or_404

from rest_framework.response import Response
from rest_framework.views import APIView
# from rest_framework.permissions import IsAuthenticated

from .serializers import BabyListSerializer, BabySerializer, BabyMeasurementSerializer
from accounts.serializers import UserBabyRelationshipSerializer, BabyAccessSerializer

from .models import Baby, BabyMeasurement
from accounts.models import User, UserBabyRelationship, Rank

# Create your views here.
class BabyListView(APIView):
    # 현 유저의 babble box들 조회
    def get(self, request):
        babies = Baby.objects.all()
        serializer = BabySerializer(babies, many=True)
        return Response(serializer.data)

    # 새로운 babble box 생성
    def post(self, request):
        baby_serializer = BabySerializer(data=request.data['baby'])
        if baby_serializer.is_valid(raise_exception=True):
            baby_serializer.save()
            # user_baby_relationship 만들기 
            baby_id = baby_serializer.data['id']
            baby = get_object_or_404(Baby, id=baby_id)
            owner = get_object_or_404(Rank, id=1)
            user_id = get_object_or_404(User, email=request.user).id
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
    # 개별 애기 정보 조회 (해당 babble box 회원들만 조회 가능)
    def get(self, request, baby_id):
        members = UserBabyRelationship.objects.filter(baby=baby_id).values_list('user', flat=True)
        user_id = get_object_or_404(User, email=request.user).id
        if user_id in members:
            baby = get_object_or_404(Baby, id=baby_id)
            serializer = BabySerializer(baby)
            return Response(serializer.data)
        return Response({'detail': '권한이 없습니다.'})

    # 개별 애기 정보 수정(해당 babble box 생성자만 수정 가능)
    def put(self, request, baby_id):
        owner = get_object_or_404(UserBabyRelationship, baby=baby_id, rank=1).user
        if owner == request.user:
            baby = get_object_or_404(Baby, id=baby_id)
            serializer = BabySerializer(baby, data=request.data)
            if serializer.is_valid():
                serializer.save()
            return Response(serializer.errors)
        return Response({'detail': '권한이 없습니다.'})

    # babble box 삭제 (해당 babble box 생성자만 삭제 가능)
    def delete(self, request, baby_id):
        owner = get_object_or_404(UserBabyRelationship, baby=baby_id, rank=1).user
        baby = get_object_or_404(Baby, id=baby_id)
        if owner == request.user:
            baby.delete()
            return Response()
        return Response({'detail': '권한이 없습니다.'})


class UserBabyRelationshipListView(APIView):
    # 현재 babble box에 초대된 유저들의 애기와의 관계 정보 조회
    def get(self, request):
        baby = request.user.current_baby
        user_baby_relationships = UserBabyRelationship.objects.filter(baby=baby).all()
        serializer = UserBabyRelationshipSerializer(user_baby_relationships, many=True)
        return Response(serializer.data)

    # 새로운 유저를 babble box에 초대
    def post(self, request):
        serializer = UserBabyRelationshipSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(baby=request.user.current_baby)
            return Response(serializer.data)
        return Response(serializer.errors)


class UserBabyRelationshipDetailView(APIView):
    # 특정 유저의 babble box 내에서의 rank/relationship_name 수정
    def put(self, request, user_id):
        baby = request.user.current_baby
        user_baby_relationship = get_object_or_404(UserBabyRelationship, user=user_id, baby=baby)
        new_rank = get_object_or_404(Rank, id=request.data['rank'])
        user_baby_relationship.rank = new_rank
        user_baby_relationship.relationship_name = request.data['relationship_name']
        user_baby_relationship.save()
        serializer = UserBabyRelationshipSerializer(user_baby_relationship)
        return Response(serializer.data)

    # 특정 유저를 babble box에서 삭제
    def delete(self, request, user_id):
        baby = request.user.current_baby
        user_baby_relationship = get_object_or_404(UserBabyRelationship, user=user_id, baby=baby)
        user_baby_relationship.delete()
        return Response()


class MyBabbleBoxView(APIView):
    # 현 유저의 user baby relationship들 조회 
    def get(self, request):
        user_id = get_object_or_404(User, email=request.user).id
        user_baby_relationships = UserBabyRelationship.objects.filter(user=user_id).all()
        serializer = UserBabyRelationshipSerializer(user_baby_relationships, many=True)
        return Response(serializer.data)


class MeasurementListView(APIView):
    # 성장 기록 전체 목록 조회
    def get(self, request):
        measurements = BabyMeasurement.objects.filter(baby=request.user.current_baby).all()
        serializer = BabyMeasurementSerializer(measurements, many=True)
        return Response(serializer.data)

    # 새로운 성장 기록 작성
    def post(self, request):
        if BabyMeasurement.objects.filter(measure_date=request.data['measure_date']).exists():
            print('수정')
            measurement = get_object_or_404(BabyMeasurement, measure_date=request.data['measure_date'])
            serializer = BabyMeasurementSerializer(measurement, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save(baby=request.user.current_baby, modifier=request.user)
                return Response(serializer.data)
            return Response(serializer.errors)
        else:
            print('생성')
            serializer = BabyMeasurementSerializer(data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save(baby=request.user.current_baby, creator=request.user)
                return Response(serializer.data)
            return Response(serializer.errors)


class MeasurementDetailView(APIView):
    # 성장 기록 detail 조회
    def get(self, request, measurement_id):
        measurement = get_object_or_404(BabyMeasurement, id=measurement_id)
        serializer = BabyMeasurementSerializer(measurement)
        return Response(serializer.data)

    # 성장 기록 수정
    def put(self, request, measurement_id):
        measurement = get_object_or_404(BabyMeasurement, id=measurement_id)
        serializer = BabyMeasurementSerializer(measurement, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(baby=request.user.current_baby, modifier=request.user)
            return Response(serializer.data)
        return Response(serializer.errors)
        
    # 성장 기록 삭제
    def delete(self, request, measurement_id):
        measurement = get_object_or_404(BabyMeasurement, id=measurement_id)
        measurement.delete()
        return Response({"message": "성장 기록이 삭제되었습니다."})


class MeasurementCheckView(APIView):
    def post(self, request):
        if BabyMeasurement.objects.filter(baby=request.user.current_baby, measure_date=request.data['measure_date']).exists():
            return Response({"exists": True})
        else:
            return Response({"exists": False})