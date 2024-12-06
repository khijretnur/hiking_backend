from rest_framework.mixins import ListModelMixin
from rest_framework.viewsets import GenericViewSet
from tags.serializers import TagSerializer
from tags.models import Tag


class TagListView(ListModelMixin, GenericViewSet):
    serializer_class = TagSerializer
    queryset = Tag.objects.order_by('position')
