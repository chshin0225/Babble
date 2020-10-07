from django.urls import path
from . import views

app_name = 'photos'

urlpatterns = [
    # photo
    path('', views.PhotoListView.as_view()),
    path('<int:photo_id>/', views.PhotoDetailView.as_view()),
    path('<int:photo_id>/comments/', views.PhotoCommentListView.as_view()),
    path('<int:photo_id>/comments/<int:comment_id>/', views.PhotoCommentDetailView.as_view()),

    # tag
    path('tags/', views.TagListView.as_view()),
    path('babblebox/tags/', views.BabyTagView.as_view()),
    path('search/', views.PhotoSearchView.as_view()),
    path('emotions/', views.PhotoEmotionView.as_view()),

    # album
    path('albums/', views.AlbumListView.as_view()),
    path('albums/<int:album_id>/', views.AlbumDetailView.as_view()),
    path('albums/<int:album_id>/photo/simple/', views.AlbumPhotoListView.as_view()),
    path('albums/<int:album_id>/photo/', views.AlbumPhotoView.as_view()),
]