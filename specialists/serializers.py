from rest_framework import serializers
from specialists.models import Specialist


class SpecialistSerializer(serializers.ModelSerializer):

    class Meta:
        model = Specialist
        fields = ('id', 'full_name', 'description', 'experience', 'image')
