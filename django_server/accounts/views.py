from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import JsonResponse
from .serializers import UserSerializer, SocialRegisterSerializer, GroupListSerializer, BabyAccessSerializer, UserBabyRelationshipSerializer
from .models import User, Group, BabyAccess, UserBabyRelationship
from babies.models import Baby
from rest_framework.authtoken.models import Token
import datetime

class CustomLoginView(APIView):
    def post(self, request):
        data = request.data
        userset = User.objects.filter(email=data['email'])
        if len(userset):
            user = userset[0]
            if user.user_type == data['user_type']:
                user.last_login = datetime.datetime.now()
                user.save()
                tokenset = Token.objects.filter(user_id=user.id)
                if len(tokenset):
                    token = tokenset[0]
                    token.delete()
                token = Token.objects.create(user=user)
                return Response({"key": token.key, "state": "login"})
            else:
                return JsonResponse({"message":"이미 가입된 이메일입니다."}, status=400)
        else:
            serializer = SocialRegisterSerializer(data=data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
            user = get_object_or_404(User, email=data['email'])
            user.last_login = datetime.datetime.now()
            user.save()
            token = Token.objects.create(user=user)
            return Response({"key": token.key, "state": "signup"})
        
class UserDetailView(APIView):
    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)

class BabyAccessView(APIView):
    # 현재 유저의 지난 babble box 접속 데이터 가져오기
    def get(self, request):
        access_log = BabyAccess.objects.filter(user=request.user).all()
        serializer = BabyAccessSerializer(access_log, many=True)
        return Response(serializer.data)

    # 현재 유저가 새로운 babble box로 이동했을 때 BabyAccess에 log 추가
    def post(self, request):
        serializer = BabyAccessSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user)

            # 유저 정보에서 current_baby 업데이트
            user = request.user
            baby = get_object_or_404(Baby, id=request.data['baby'])
            user.current_baby = baby
            user.save()

            return Response(serializer.data)
        return Response(serializer.errors)

class GroupListView(APIView):
    # 한 babble box 내의 존재하는 그룹들 조회
    def get(self, request):
        baby = request.user.current_baby
        groups = Group.objects.filter(baby=baby).all()
        serializer = GroupListSerializer(groups, many=True)
        return Response(serializer.data)

    # 새로운 그룹 생성
    def post(self, request):
        baby = request.user.current_baby
        serializer = GroupListSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(baby=baby)
            return Response(serializer.data)
        return Response(serializer.errors)

class GroupDetailView(APIView):
    # 한 그룹 내의 유저 목록 조회
    def get(self, request, group_id):
        group_members = UserBabyRelationship.objects.filter(group=group_id).all()
        serializer = UserBabyRelationshipSerializer(group_members, many=True)
        return Response(serializer.data)
    
    # 그룹에 유저 추가(초대하려는 유저는 babble box 멤버여야함)
    def put(self, request, group_id):
        baby = request.user.current_baby
        user = get_object_or_404(User, id=request.data['user']).id
        group = get_object_or_404(Group, id=group_id)
        data = get_object_or_404(UserBabyRelationship, baby=baby, user=user)
        data.group = group
        data.save()
        serializer = UserBabyRelationshipSerializer(data)
        return Response(serializer.data)

    # 그룹에서 멤버 제거
    def delete(self, request, group_id):
        baby = request.user.current_baby
        user = get_object_or_404(User, id=request.data['user']).id
        group = get_object_or_404(Group, id=group_id)
        data = get_object_or_404(UserBabyRelationship, baby=baby, user=user)
        data.group = None
        data.save()
        serializer = UserBabyRelationshipSerializer(data)
        return Response(serializer.data)