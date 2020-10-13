from rest_framework import serializers
from .models import Baby, BabyMeasurement

class BabyListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Baby
        fields = ['id', 'baby_name', 'birth', 'profile_image']

class BabySerializer(serializers.ModelSerializer):
    class Meta:
        model = Baby
        fields = '__all__'

class BabyMeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = BabyMeasurement
        fields = '__all__'


class WeightMeasurementSerializer(serializers.ModelSerializer):
    x = serializers.SerializerMethodField('get_measure_date')
    y = serializers.SerializerMethodField('get_weight')
    class Meta:
        model = BabyMeasurement
        fields = ['x', 'y']

    def get_measure_date(self, measurement):
        return measurement.measure_date

    def get_weight(self, measurement):
        return measurement.weight


class HeightMeasurementSerializer(serializers.ModelSerializer):
    x = serializers.SerializerMethodField('get_measure_date')
    y = serializers.SerializerMethodField('get_height')
    class Meta:
        model = BabyMeasurement
        fields = ['x', 'y']

    def get_measure_date(self, measurement):
        return measurement.measure_date

    def get_height(self, measurement):
        return measurement.height


class HeadMeasurementSerializer(serializers.ModelSerializer):
    x = serializers.SerializerMethodField('get_measure_date')
    y = serializers.SerializerMethodField('get_head_size')
    class Meta:
        model = BabyMeasurement
        fields = ['x', 'y']

    def get_measure_date(self, measurement):
        return measurement.measure_date

    def get_head_size(self, measurement):
        return measurement.head_size