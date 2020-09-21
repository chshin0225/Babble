from django.urls import path
from . import views

app_name = 'photos'

urlpatterns = [
    path('', views.PhotoListView.as_view()),
    path('<int:photo_id>/', views.PhotoDetailView.as_view()),
]