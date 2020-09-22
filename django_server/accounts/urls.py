from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    # path('signup/', views.SignUpView.as_view(), name='signup'), 
    # # path('/signin', views.SignInView.as_view()),
    # path('activate/<str:uidb64>/<str:token>/', views.Activate.as_view(), name='activate'),

    # path('login/kakao/', views.kakao_login, name='kakao_login'),
    # path('login/kakao/callback/', views.kakao_callback, name='kakao_callback')
    path('myinfo/', views.UserDetailView.as_view()),
    path('access/', views.BabyAccessView.as_view()),
    path('groups/', views.GroupListView.as_view()),
    path('groups/<int:group_id>/', views.GroupDetailView.as_view()),
]