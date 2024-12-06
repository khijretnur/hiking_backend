from rest_framework import serializers
from recommendations import models


class RecommendationListSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Recommendation
        exclude = ('category', 'created_at', 'updated_at')


class RecommendationCategorySerializer(serializers.ModelSerializer):
    recommendations = RecommendationListSerializer(many=True)

    class Meta:
        model = models.RecommendationCategory
        exclude = ('created_at', 'updated_at')


class RecommendationFileSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.RecommendationFile
        exclude = ('recommendation', 'created_at', 'updated_at')


class RecommendationDetailSerializer(serializers.ModelSerializer):
    files = RecommendationFileSerializer(many=True)

    class Meta:
        model = models.Recommendation
        exclude = ('created_at', 'updated_at')
