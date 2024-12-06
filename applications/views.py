from rest_framework.mixins import CreateModelMixin
from rest_framework.viewsets import GenericViewSet
from applications.serializers import ApplicationSerializer
from applications.models import Application


class ApplicationCreateView(CreateModelMixin, GenericViewSet):
    serializer_class = ApplicationSerializer
    queryset = Application.objects.order_by()
