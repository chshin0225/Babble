from django.urls import path
from . import views

app_name = 'babies'

urlpatterns = [
    path('', views.BabyListView.as_view()),
    path('<int:baby_id>/', views.BabyDetailView.as_view()),
    
    # 한 babble box 내의 유저들 관리 관련
    path('relationships/', views.UserBabyRelationshipListView.as_view()),
    path('relationships/<int:user_id>/', views.UserBabyRelationshipDetailView.as_view()),
    
    # 내가 초대된 babble box들 정보 관련
    path('mybabblebox/', views.MyBabbleBoxView.as_view()),
]