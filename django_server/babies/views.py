from django.shortcuts import render, get_object_or_404

from rest_framework.response import Response
from rest_framework.views import APIView
# from rest_framework.permissions import IsAuthenticated

from .serializers import BabyListSerializer, BabySerializer, BabyMeasurementSerializer
from accounts.serializers import UserBabyRelationshipSerializer

from .models import Baby
from accounts.models import UserBabyRelationship, Rank

# Create your views here.
class BabyListView(APIView):
    # permission_classes = ['IsAuthenticated']
    def get(self, request):
        # my_babies = UserBabyRelationship.objects.filter(user=request.user).values('baby_id')
        my_babies = UserBabyRelationship.objects.all()
        print(my_babies)
        babies = Baby.objects.all()
        serializer = BabyListSerializer(babies, many=True)
        return Response(serializer.data)
    
    # 새로운 babble box 생성
    def post(self, request):
        baby_serializer = BabySerializer(data=request.data['baby'])
        if baby_serializer.is_valid(raise_exception=True):
            baby_serializer.save()
            # print(baby_serializer.data)
            # print(request.user)
            baby_id = baby_serializer.data['id']
            # print(baby_id)
            baby = Baby.objects.get(id=baby_id)
            owner = Rank.objects.get(id=1)
            print(request.user)
            user_baby_relationship = {
                # 'user': request.user['id'],
                'user': 1,
                'relationship_name': request.data['relationship_name']
            }
            relationship_serializer = UserBabyRelationshipSerializer(data=user_baby_relationship)
            if relationship_serializer.is_valid(raise_exception=True):
                relationship_serializer.save(baby=baby, rank=owner)
                return Response(relationship_serializer.data)
            return Response(relationship_serializer.errors)
        return Response(serializer.errors)


class BabyDetailView(APIView):
    def get(self, request, baby_id):
        baby = Baby.objects.get(id=baby_id)
        serializer = BabySerializer(baby)
        return Response(serializer.data)

    def put(self, request, baby_id):
        pass

    def delete(self, request, baby_id):
        pass


class UserBabyRelationshipListView(APIView):
    def get(self, request):
        # user_baby_relationships = UserBabyRelationship.objects.filter(user=request.user).all()
        user_baby_relationships = UserBabyRelationship.objects.all()
        serializer = UserBabyRelationshipSerializer(user_baby_relationships, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = UserBabyRelationshipSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)