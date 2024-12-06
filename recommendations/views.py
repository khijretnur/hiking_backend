from django.db.models import Prefetch
from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import action
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from recommendations import serializers, models
from utils.schema import QUERY_RECOMMENDATION_ID


class RecommendationCategoryListView(ListModelMixin, GenericViewSet):
    serializer_class = serializers.RecommendationCategorySerializer
    queryset = models.RecommendationCategory.objects.order_by()

    def get_queryset(self):
        return models.RecommendationCategory.objects.prefetch_related('recommendations')


class RecommendationRetrieveView(RetrieveModelMixin, GenericViewSet):
    serializer_class = serializers.RecommendationDetailSerializer
    queryset = models.Recommendation.objects.order_by()

    def get_queryset(self):
        return models.Recommendation.objects.prefetch_related(
            Prefetch(
                'files',
                queryset=models.RecommendationFile.objects.order_by('position')
            )
        )


class RecommendationExcludeView(ListModelMixin, GenericViewSet):
    serializer_class = serializers.RecommendationListSerializer
    queryset = models.Recommendation.objects.order_by()

    @swagger_auto_schema(manual_parameters=[QUERY_RECOMMENDATION_ID]
                         )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    def get_queryset(self):
        exclude_id = self.request.query_params.get('recommendation_id', None)
        if exclude_id:
            return models.Recommendation.objects.exclude(id=exclude_id)
        return models.Recommendation.objects.order_by()
