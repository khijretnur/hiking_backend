from rest_framework.mixins import ListModelMixin
from rest_framework.viewsets import GenericViewSet
from specialists.serializers import SpecialistSerializer
from specialists.models import Specialist


class SpecialistViewSet(ListModelMixin, GenericViewSet):
    serializer_class = SpecialistSerializer
    queryset = Specialist.objects.order_by('-id')
