from rest_framework import serializers
from services.models import Service, ServiceImage


class ServiceListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Service
        fields = ('id', 'name', 'image')


class ServiceImageSerializer(serializers.Serializer):
    image = serializers.ImageField()


class ServiceDetailSerializer(serializers.ModelSerializer):
    images = ServiceImageSerializer(many=True)

    class Meta:
        model = Service
        fields = ('id', 'name', 'image', 'images', 'text', 'detail_image' , 'description')
