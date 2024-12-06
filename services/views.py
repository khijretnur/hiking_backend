from django.db.models import Prefetch
from drf_yasg.utils import swagger_auto_schema
from rest_framework.viewsets import GenericViewSet
from services import serializers
from services import models
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin

from utils.schema import QUERY_SERVICE_ID


class ServiceViewSet(ListModelMixin, RetrieveModelMixin, GenericViewSet):
    serializer_class = serializers.ServiceListSerializer
    queryset = models.Service.objects.order_by('position')

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return serializers.ServiceDetailSerializer
        return super(ServiceViewSet, self).get_serializer_class()

    def get_queryset(self):
        queryset = models.Service.objects.order_by('position')
        if self.action == 'retrieve':
            queryset = queryset.prefetch_related(
                Prefetch('images', queryset=models.ServiceImage.objects.order_by('position'))
            )
        return queryset


class ServiceExcludeList(ListModelMixin, GenericViewSet):
    serializer_class = serializers.ServiceListSerializer
    queryset = models.Service.objects.order_by('position')

    @swagger_auto_schema(manual_parameters=[QUERY_SERVICE_ID]
                         )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    def get_queryset(self):
        exclude_id = self.request.query_params.get('service_id', None)
        if exclude_id:
            return models.Service.objects.exclude(id=exclude_id)
        return models.Service.objects.order_by()
