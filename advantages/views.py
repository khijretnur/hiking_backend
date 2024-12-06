from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin
from advantages import models, serializers


class AdvantageListView(ListModelMixin, GenericViewSet):
    pagination_class = None
    queryset = models.Advantage.objects.order_by('id')
    serializer_class = serializers.AdvantageSerializer
