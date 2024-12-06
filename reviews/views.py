from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin
from reviews.serializers import ReviewSerializer
from reviews.models import Review


class ReviewListView(ListModelMixin, GenericViewSet):
    serializer_class = ReviewSerializer
    queryset = Review.objects.select_related('tour').order_by('-id')

    def filter_queryset(self, queryset):
        extra_kwargs = {}
        if self.request.query_params.get('tour_id'):
            extra_kwargs['tour_id'] = self.request.query_params.get('tour_id')

        return queryset.filter(**extra_kwargs)
