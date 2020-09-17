from django.shortcuts import render, get_object_or_404

from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import BabyListSerializer, BabySerializer, BabyMeasurementSerializer
from accounts.serializers import UserBabyRelationshipSerializer

from .models import Baby
from accounts.models import UserBabyRelationship

# Create your views here.
class BabyListView(APIView):
    def get(self, request):
        # my_babies = UserBabyRelationship.objects.filter(user=request.user).values('baby_id')
        my_babies = UserBabyRelationship.objects.all()
        print(my_babies)
        babies = Baby.objects.all()
        serializer = BabyListSerializer(babies, many=True)
        return Response(serializer.data)
    
    # 새로운 babble box 생성
    def post(self, request):
        serializer = BabySerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


class BabyDetailView(APIView):
    def get(self, request, baby_id):
        pass

    def put(self, request, baby_id):
        pass

    def delete(self, request, baby_id):
        pass
