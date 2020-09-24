from django.urls import path
from . import views

app_name = 'babies'

urlpatterns = [
    # 애기 정보 관련
    path('', views.BabyListView.as_view()),
    path('<int:baby_id>/', views.BabyDetailView.as_view()),
    
    # 한 babble box 내의 유저들 관리 관련
    path('relationships/', views.UserBabyRelationshipListView.as_view()),
    path('relationships/<int:user_id>/', views.UserBabyRelationshipDetailView.as_view()),
    
    # 내가 초대된 babble box들 정보 관련
    path('mybabblebox/', views.MyBabbleBoxView.as_view()),

    # 성장 기록 관련
    path('measurements/', views.MeasurementListView.as_view()),
    path('measurements/<int:measurement_id>/', views.MeasurementDetailView.as_view()),
    path('measurements/check/', views.MeasurementCheckView.as_view()),
]