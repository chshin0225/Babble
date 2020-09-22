from django.shortcuts import render, get_object_or_404

from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import UserSerializer, GroupListSerializer, BabyAccessSerializer, UserBabyRelationshipSerializer

from .models import User, Group, BabyAccess, UserBabyRelationship
from babies.models import Baby

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
            baby = Baby.objects.get(id=request.data['baby'])
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
        user = User.objects.get(id=request.data['user']).id
        group = Group.objects.get(id=group_id)
        data = UserBabyRelationship.objects.get(baby=baby, user=user)
        data.group = group
        data.save()
        serializer = UserBabyRelationshipSerializer(data)
        return Response(serializer.data)

    # 그룹에서 멤버 제거
    def delete(self, request, group_id):
        baby = request.user.current_baby
        user = User.objects.get(id=request.data['user']).id
        group = Group.objects.get(id=group_id)
        data = UserBabyRelationship.objects.get(baby=baby, user=user)
        data.group = None
        data.save()
        serializer = UserBabyRelationshipSerializer(data)
        return Response(serializer.data)









# from rest_framework import generics, views, status, permissions
# from rest_framework.response import Response

# from django.utils.encoding import force_text
# from django.utils.http import urlsafe_base64_decode
# from django.shortcuts import render, redirect
# from rest_framework.views import APIView

# from . import models, serializers, token

# import urllib


# # 자체 구현
# import jwt
# import json

# from .models import User
# from .token import account_activation_token
# from .text import message

# from django.views import View
# from django.http import HttpResponse, JsonResponse
# from django.core.exceptions import ValidationError
# from django.core.validators import validate_email
# from django.shortcuts import redirect
# from django.contrib.sites.shortcuts import get_current_site
# from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
# from django.core.mail import EmailMessage
# from django.utils.encoding import force_bytes, force_text

# class SignUpView(View):
#     def post(self, request):
#         data = json.loads(request.body)
#         try:
#             validate_email(data["email"])

#             if User.objects.filter(email=data["email"]).exists():
#                 return JsonResponse({"message":"EXISTS_EMAIL"}, status=400)

#             user = User.objects.create(
#                 email = data["email"],
#                 password = bcrypt.hashpw(data["password"].encode("UTF-8"), bcrypt.gensalt()).decode("UTF-8"),
#                 is_active = False
#             )

#             current_site = get_current_site(request)
#             domain = current_site.domain
#             uidb64 = urlsafy_base64_encode(force_bytes(user.pk))
#             token = account_activation_token.make_token(user)
#             message_data = message(domain, uid64, token)

#             mail_title = "이메일 인증을 완료해주세요!"
#             mail_to = data['email']
#             email = EmailMessage(mail_title, message_data, to=[mail_to])
#             email.send()

#             return JsonResponse({"message":"SUCCESS"}, status=200)
        
#         except KeyError:
#             return JsonResponse({"message":"INVALID_KEY"}, status=400)
#         except TypeError:
#             return JsonResponse({"message":"INVALID_TYPE"}, status=400)
#         except ValidationError:
#             return JsonResponse({"message":"VALIDATION_ERROR"}, status=400)


# class Activate(View):
#     def get(self, request, uidb64, token):
#         try:
#             uid = force_text(urlsafe_base64_decode(uidb64))
#             user = User.objects.get(pk=uid)

#             if account_activation_token.check_token(user, token):
#                 user.is_active = True
#                 user.save()

#                 return redirect('/')

#             return JsonResponse({"message" : "AUTH FAIL"}, status=400)
        
#         except KeyError:
#             return JsonResponse({"message" : "INVALID_KEY"}, status=400)
#         except ValidationError:
#             return JsonResponse({"message" : "TYPE_ERROR"}, status=400)
        









# # code 요청
# def kakao_login(request):
#     app_rest_api_key = '6b1c8dd547b0885585c9f4e21d64d1f2',
#     redirect_uri = "http://127.0.0.1:8000/accounts/login/kakao/callback"
#     return redirect(
#         f"https://kauth.kakao.com/oauth/authorize?client_id={app_rest_api_key}&redirect_uri={redirect_uri}&response_type=code"
#     )
    
    
# # access token 요청
# def kakao_callback(request):                                                                  
#     params = urllib.parse.urlencode(request.GET)                                      
#     return redirect(f'http://127.0.0.1:8000/accounts/login/kakao/callback?{params}') 