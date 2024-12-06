from rest_framework import serializers
from advantages import models


class AdvantageSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Advantage
        fields = ('id', 'title', 'text', 'icon')
