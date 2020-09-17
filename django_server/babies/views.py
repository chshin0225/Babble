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
        baby_serializer = BabySerializer(data=request.data)
        if baby_serializer.is_valid(raise_exception=True):
            baby_serializer.save()
            return Response(baby_serializer.data)
        return Response(serializer.errors)


class BabyDetailView(APIView):
    def get(self, request, baby_id):
        pass

    def put(self, request, baby_id):
        pass

    def delete(self, request, baby_id):
        pass


class UserBabyRelationshipListView(APIView):
    def get(self, request):
        user_baby_relationships = UserBabyRelationship.objects.filter(user=request.user).all()
        serializer = UserBabyRelationshipSerializer(user_baby_relationships, many=True)
        return Response(serializer.data)

    def put(self, request):
        pass