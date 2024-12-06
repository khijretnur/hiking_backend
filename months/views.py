from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.mixins import ListModelMixin
from rest_framework.viewsets import GenericViewSet
from months import models, serializers


class MonthListView(ListModelMixin, GenericViewSet):
    serializer_class = serializers.MonthSerializer
    queryset = models.Month.objects.order_by('month_num')
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['season']
