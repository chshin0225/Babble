from django.urls import path
from . import views

app_name = 'diaries'

urlpatterns = [
    path('', views.DiaryListView.as_view()),
    path('<int:diary_id>/', views.DiaryDetailView.as_view()),
]