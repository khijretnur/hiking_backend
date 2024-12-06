from rest_framework import serializers
from reviews.models import Review


class ReviewTourSerializer(serializers.Serializer):
    name = serializers.CharField()


class ReviewSerializer(serializers.ModelSerializer):
    tour = ReviewTourSerializer()

    class Meta:
        model = Review
        exclude = ('created_at', 'updated_at', 'author_kk',
                   'author_ru', 'author_en', 'text_kk', 'text_ru', 'text_en'
                   )

