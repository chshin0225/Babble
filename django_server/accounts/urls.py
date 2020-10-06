from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('login/social/', views.CustomLoginView.as_view(), name='social_login'),
    path('myinfo/', views.UserDetailView.as_view()),
    path('profilechange/', views.UserDetailView.as_view()),
    path('access/', views.BabyAccessView.as_view()),
    path('invitation/', views.InvitationCreateView.as_view()),
    path('invitation/<str:token>/', views.InvitationVerifyView.as_view()),

    # 현재 babble box에 속한 유저들 정보 관련
    path('groups/', views.GroupListView.as_view()),
    path('groups/<int:group_id>/', views.GroupDetailView.as_view()),
    path('groups/<int:group_id>/info/', views.GroupInfoView.as_view()),
]