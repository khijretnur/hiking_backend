from rest_framework import serializers
from countries.models import Country


class CountrySerializer(serializers.ModelSerializer):
    tours_count = serializers.IntegerField(default=0)

    class Meta:
        model = Country
        fields = ('id', 'name', 'image', 'tours_count')


class SimpleCountrySerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
