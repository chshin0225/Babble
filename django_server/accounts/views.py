from django.shortcuts import render, get_object_or_404

from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import JsonResponse
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
    
    # 그룹에 유저 추가
    def put(self, request, group_id):
        baby = request.user.current_baby
        user = UserBabyRelationship.objects.get(baby=baby, user=request.data['user'])
        serializer = UserBabyRelationshipSerializer(data=request.data)

    def delete(self, request, group_id):
        pass









# from rest_framework import generics, views, status, permissions
# from rest_framework.response import Response

# from django.utils.encoding import force_text
# from django.utils.http import urlsafe_base64_decode

# from rest_framework.views import APIView

# from . import models, serializers, token




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
        





from django.shortcuts import render, redirect
import urllib
import json
with open("./secrets.json") as f:
    secrets = json.loads(f.read())

# code 요청
def kakao_login(request):
    app_rest_api_key = secrets['OAUTH']['KAKAO']['CLIENT_ID']
    # redirect_uri = "http://127.0.0.1:8000/accounts/login/kakao/callback"
    redirect_uri = "http://j3a310.p.ssafy.io:8000/accounts/login/kakao/callback"
    # redirect_uri = "http://localhost:8080/login/kakao"
    return redirect(
        f"https://kauth.kakao.com/oauth/authorize?client_id={app_rest_api_key}&redirect_uri={redirect_uri}&response_type=code"
    )
    

from rest_auth.registration.views import SocialLoginView                   
from allauth.socialaccount.providers.kakao import views as kakao_views     
from allauth.socialaccount.providers.oauth2.client import OAuth2Client     
import requests                       
from django.shortcuts import redirect 
from .models import User
from rest_framework.authtoken.models import Token


class KakaoException(Exception):
    pass

# access token 요청
def kakao_callback(request):

    try:
        app_rest_api_key = secrets['OAUTH']['KAKAO']['CLIENT_ID']
        # redirect_uri = "http://127.0.0.1:8000/accounts/login/kakao/callback"
        redirect_uri = "http://j3a310.p.ssafy.io:8000/accounts/login/kakao/callback"
        # redirect_uri = "http://localhost:8080/login/kakao"


        user_token = request.GET.get("code")

        # post request
        token_request = requests.get(
            f"https://kauth.kakao.com/oauth/token?grant_type=authorization_code&client_id={app_rest_api_key}&redirect_uri={redirect_uri}&code={user_token}"
        )
        token_response_json = token_request.json()
        error = token_response_json.get("error", None)
        
        # if there is an error from token_request
        if error is not None:
            raise KakaoException()
        access_token = token_response_json.get("access_token")
		
        # post request
        profile_request = requests.post(
            "https://kapi.kakao.com/v2/user/me",
            headers={"Authorization": f"Bearer {access_token}"},
        )
        profile_json = profile_request.json()

        # parsing profile json
        user_id = profile_json.get("id")
        kakao_account = profile_json.get("kakao_account")
        email = kakao_account.get("email", None)
        if email is None:
            email = f"nobabbleemail_{user_id}@babble.com"
        #     raise KakaoException()   # 이메일은 필수제공 항목이 아니므로 수정 필요 (비즈니스 채널을 연결하면 검수 신청 후 필수 변환 가능)
        profile = kakao_account.get("profile")
        nickname = profile.get("nickname")
        profile_image = profile.get("thumbnail_image_url")   # 사이즈 'thumbnail_image_url' < 'profile_image_url'

        try:   
            user_in_db = User.objects.get(email=email)
            # kakao계정 email이 서비스에 이미 따로 가입된 email 과 충돌한다면
            if user_in_db.user_type != 'kakao':
                raise KakaoException()
            # 이미 kakao로 가입된 유저라면
            else:
                # 서비스에 rest-auth 로그인
                data = {'code': user_token, 'access_token': access_token}
                accept = requests.post(
                    f"http://127.0.0.1:8000/accounts/login/kakao/todjango/", data=data
                )
                # accept_jwt = accept_json.get("token")

                accept_json = accept.json()
                current_token = get_object_or_404(Token, key=accept_json['key'])
                User.objects.filter(id=current_token.user_id).update(name=nickname,
                                                    email=email,
                                                    user_type='kakao',
                                                    profile_image=profile_image,
                                                    is_active=True
                                                    )

        except User.DoesNotExist:
            # 서비스에 rest-auth 로그인
            data = {'code': user_token, 'access_token': access_token}
            accept = requests.post(
                f"http://127.0.0.1:8000/accounts/login/kakao/todjango/", data=data
            )

            accept_json = accept.json()
            current_token = get_object_or_404(Token, key=accept_json['key'])
            User.objects.filter(id=current_token.user_id).update(name=nickname,
                                                    email=email,
                                                    user_type='kakao',
                                                    profile_image=profile_image,
                                                    is_active=True
                                                    )
        # return Response(accept_json, status=200)
        return JsonResponse(accept_json, status=200)

    except KakaoException:
        raise KakaoException()
        # return redirect("http://127.0.0.1:8000/accounts/login")
        

class KakaoToDjangoLogin(SocialLoginView): 
    adapter_class = kakao_views.KakaoOAuth2Adapter  
    client_class = OAuth2Client 