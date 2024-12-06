from rest_framework.mixins import ListModelMixin
from rest_framework.viewsets import GenericViewSet
from banners import models, serializers


class BannerListView(ListModelMixin, GenericViewSet):
    pagination_class = None
    serializer_class = serializers.BannerSerializer
    queryset = models.Banner.objects.order_by('position')
