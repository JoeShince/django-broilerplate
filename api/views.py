from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, serializers

from api.models import SampleModel


class SampleSerializer(serializers.ModelSerializer):
    class Meta:
        model = SampleModel
        fields = '__all__'


class SampleViewSets(viewsets.ModelViewSet):
    serializer_class = SampleSerializer

