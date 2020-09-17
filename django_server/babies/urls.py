from django.urls import path
from . import views

app_name = 'babies'

urlpatterns = [
    path('', views.BabyListView.as_view()),
    path('<int:baby_id>/', views.BabyDetailView.as_view()),
    path('relationships/', views.UserBabyRelationshipListView.as_view()),
]