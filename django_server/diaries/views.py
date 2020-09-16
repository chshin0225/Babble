from django.shortcuts import render

from rest_framework.response import Response 
from rest_framework.views import APIView

from .serializers import DiaryListSerializer
from .models import Diary

# Create your views here.
class DiaryListView(APIView):
    def get(self, request):
        # baby id 데이터 어디서? 프론트가 보내줘야할듯
        diaries = Diary.objects.filter(baby=1)
        serializer = DiaryListSerializer(diaries, many=True)
        return Response(serializer.data)

    def post(self, request):
        pass

class DiaryDetailView(APIView):
    def get(self, request):
        pass

    def put(self, request):
        pass

    def delete(self, request):
        pass