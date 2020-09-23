from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('login/social/', views.CustomLoginView.as_view(), name='social_login'),
    path('myinfo/', views.UserDetailView.as_view()),
    path('access/', views.BabyAccessView.as_view()),
    path('groups/', views.GroupListView.as_view()),
    path('groups/<int:group_id>/', views.GroupDetailView.as_view()),
]