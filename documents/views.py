from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from documents.serializers import DocumentSerializer, PrivacyStatementSerializer
from documents.models import Document, PrivacyStatement


class DocumentViewSet(ListModelMixin, RetrieveModelMixin, GenericViewSet):
    serializer_class = DocumentSerializer
    queryset = Document.objects.order_by('position')


class PrivacyStatementViewSet(ListModelMixin, RetrieveModelMixin, GenericViewSet):
    pagination_class = None
    serializer_class = PrivacyStatementSerializer
    queryset = PrivacyStatement.objects.order_by()
