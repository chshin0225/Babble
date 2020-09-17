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