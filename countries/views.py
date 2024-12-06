from django.db.models import Count, Sum
from rest_framework.mixins import ListModelMixin
from rest_framework.viewsets import GenericViewSet
from countries.serializers import CountrySerializer, SimpleCountrySerializer
from countries.models import Country


class CountryListView(ListModelMixin, GenericViewSet):
    serializer_class = CountrySerializer
    queryset = Country.objects.order_by('position')

    def get_queryset(self):
        return Country.objects.order_by('position').annotate(tours_count=Count('tours'))


class SimpleCountryListView(ListModelMixin, GenericViewSet):
    serializer_class = SimpleCountrySerializer
    queryset = Country.objects.order_by('position')
