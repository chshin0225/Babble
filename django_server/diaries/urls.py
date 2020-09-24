from django.urls import path
from . import views

app_name = 'diaries'

urlpatterns = [
    path('', views.DiaryListView.as_view()),
    path('photo/', views.DiaryPhotoListView.as_view()),
    path('<int:diary_id>/', views.DiaryDetailView.as_view()),
    path('<int:diary_id>/comments/', views.DiaryCommentListView.as_view()),
    path('<int:diary_id>/comments/<int:comment_id>/', views.DiaryCommentDetailView.as_view()),
] 