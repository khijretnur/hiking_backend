from rest_framework import serializers
from months.models import Month


class MonthSerializer(serializers.ModelSerializer):

    class Meta:
        model = Month
        exclude = ('name_kk', 'name_ru', 'name_en')
