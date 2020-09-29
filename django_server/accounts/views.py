import datetime
from operator import itemgetter
from itertools import groupby

from django.shortcuts import render, get_object_or_404

from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import UserSerializer, SocialRegisterSerializer, GroupListSerializer, BabyAccessSerializer, UserBabyRelationshipSerializer, InvitationSerializer

from .models import User, Rank, Group, BabyAccess, UserBabyRelationship, Invitation
from babies.models import Baby
from babies.serializers import BabySerializer
from rest_framework.authtoken.models import Token

import random
import string
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
                return Response({"message":"이미 가입된 이메일입니다."}, status=400)
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
        groups = list(Group.objects.filter(baby=baby).values_list('id', flat=True))
        group_data = UserBabyRelationship.objects.filter(baby=baby, group__isnull=False).values('id', 'user', 'group', 'relationship_name')

        key = itemgetter('group')
        rows = groupby(group_data, key=key)

        return_data = []
        for group, items in rows:
            items = list(items)
            group_info = get_object_or_404(Group, id=group)
            group_serializer = GroupListSerializer(group_info)
            new_group_serializer = dict(group_serializer.data)
            new_group_serializer['members'] = items
            return_data.append(new_group_serializer)
            groups.remove(group)
        
        if groups:
            for g in groups:
                group_info = get_object_or_404(Group, id=g)
                group_serializer = GroupListSerializer(group_info)
                new_group_serializer = dict(group_serializer.data)
                new_group_serializer['members'] = []
                return_data.append(new_group_serializer)

        return Response(return_data)

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

class GroupInfoView(APIView):
    # 그룹명 수정
    def put(self, request, group_id):
        group = get_object_or_404(Group, id=group_id)
        serializer = GroupListSerializer(group, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(baby=request.user.current_baby)
            return Response(serializer.data)
        return Response(serializer.errors)

    # 그룹 삭제
    def delete(self,request, group_id):
        baby = request.user.current_baby
        group = get_object_or_404(Group, id=group_id)
        group.delete()
        return Response({'message': '그룹 삭제가 완료되었습니다.'})

class InvitationCreateView(APIView):
    def post(self, request):
        print('hi')
        data = request.data
        baby = request.user.current_baby_id
        rank = data['rank']
        try:
            relationship = get_object_or_404(UserBabyRelationship, baby_id=baby, user_id=request.user.id, rank=1)
            token = ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(16))
            invite_url = "http://j3a310.p.ssafy.io/invite/" + token
            invitation = Invitation(baby_id=baby, rank_id=rank, token=token)
            invitation.save()
            return Response({"url": invite_url}, status=200)
        except:
            return Response({"message":"초대링크를 생성할 권한이 없습니다."}, status=400)

class InvitationVerifyView(APIView):
    def get(self, request, token):
        try:
            invitation = get_object_or_404(Invitation, token=token, closed=False)
            serializer = InvitationSerializer(invitation)
            return Response(serializer.data)            
        except:
            return Response({"message":"초대 링크가 유효하지 않습니다."}, status=400)

    def post(self, request, token):
        relationship_name = request.data['relationship_name']
        user = request.user
        try:
            invitation = get_object_or_404(Invitation, token=token, closed=False)
            try:
                relationship = get_object_or_404(UserBabyRelationship, baby_id=invitation.baby_id, user_id=user.id)
                relationship.rank_id = invitation.rank_id
                relationship.relationship_name = relationship_name
                relationship.save()
            except:
                relationship = UserBabyRelationship(
                                baby_id=invitation.baby_id,
                                rank_id=invitation.rank_id,
                                user_id=user.id,
                                relationship_name=relationship_name)
                relationship.save()
            baby = get_object_or_404(Baby, id=invitation.baby_id)
            user.current_baby = baby
            user.save()
            invitation.closed = True
            invitation.save()
            serializer = BabySerializer(baby)
            return Response(serializer.data)
        except:
            return Response({"message":"초대 링크가 유효하지 않습니다."}, status=400)