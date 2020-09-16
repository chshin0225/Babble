from rest_framework import serializers
from .models import Baby, BabyMeasurement
from accounts.serializers import UserSerializer

class BabySerializer(serializers.ModelSerializer):
    class Meta:
        model = Baby
        fields = '__all__'


class BabyMeasurementListSerializer(serializers.ModelSerializer):
    baby = BabySerializer(required=False)
    creator = UserSerializer(required=False)
    modifer = UserSerializer(required=False)
    class Meta:
        model = Baby
        fields = '__all__'