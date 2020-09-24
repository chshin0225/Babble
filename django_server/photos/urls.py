from django.urls import path
from . import views

app_name = 'photos'

urlpatterns = [
    path('', views.PhotoListView.as_view()),
    path('<int:photo_id>/', views.PhotoDetailView.as_view()),
    path('<int:photo_id>/comments/', views.PhotoCommentListView.as_view()),
    path('<int:photo_id>/comments/<int:comment_id>/', views.PhotoCommentDetailView.as_view()),
    path('tags/', views.TagListView.as_view()),
    path('search/', views.PhotoSearchView.as_view()),
]