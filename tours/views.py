from django.db.models import Prefetch
from drf_yasg.utils import swagger_auto_schema
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet
from tours import models
from tours.models import TourPrice, Tour
from tours.serializers import TourSerializer, TourDetailSerializer, \
    TourSeasonSerializer, TourPlacementSerializer, TourFormatSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from utils.schema import QUERY_COUNTRY_IDS, QUERY_TAG_IDS, QUERY_SEASON_IDS, QUERY_PLACEMENT_IDS, QUERY_FORMATS_IDS, \
    QUERY_DIRECTION


class TourListView(ListModelMixin, GenericViewSet):
    queryset = models.Tour.objects.order_by('-id')
    serializer_class = TourSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']

    @swagger_auto_schema(manual_parameters=[
        QUERY_COUNTRY_IDS,
        QUERY_TAG_IDS,
        QUERY_SEASON_IDS,
        QUERY_PLACEMENT_IDS,
        QUERY_FORMATS_IDS,
        QUERY_DIRECTION
    ])
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    def filter_queryset(self, queryset):
        extra_kwargs = {}
        if self.request.query_params.get('duration_start') and self.request.query_params.get('duration_end'):
            duration_start = self.request.query_params.get('duration_start')
            duration_end = self.request.query_params.get('duration_end')
            extra_kwargs['duration__gte'] = duration_start
            extra_kwargs['duration__lte'] = duration_end
        if self.request.query_params.get('budget_start') and self.request.query_params.get('budget_end'):
            budget_start = self.request.query_params.get('budget_start')
            budget_end = self.request.query_params.get('budget_end')
            extra_kwargs['budget__gte'] = budget_start
            extra_kwargs['budget__lte'] = budget_end
        if self.request.query_params.get('month'):
            month = self.request.query_params.get('month')
            extra_kwargs['dates__start_date__month'] = month

        if self.request.query_params.get('countries'):
            countries_param = self.request.query_params.get('countries')
            countries_list = [int(country_id) for country_id in countries_param.split(',')]
            extra_kwargs['country__in'] = countries_list
        if self.request.query_params.get('seasons'):
            seasons_param = self.request.query_params.get('seasons')
            seasons_list = [int(season_id) for season_id in seasons_param.split(',')]
            extra_kwargs['seasons__in'] = seasons_list
        if self.request.query_params.get('placements'):
            placements_param = self.request.query_params.get('placements')
            placements_list = [int(placement_id) for placement_id in placements_param.split(',')]
            extra_kwargs['placements__in'] = placements_list
        if self.request.query_params.get('formats'):
            formats_param = self.request.query_params.get('formats')
            formats_list = [int(format_id) for format_id in formats_param.split(',')]
            extra_kwargs['formats__in'] = formats_list
        return queryset.filter(**extra_kwargs)

    def get_queryset(self):
        return models.Tour.objects.order_by('-id').select_related('country').prefetch_related(
            'formats',
            Prefetch(
                'images',
                queryset=models.TourImage.objects.order_by('position')
            ),
            Prefetch(
                'dates',
                queryset=models.TourDate.objects.order_by('start_date')
            )
        ).distinct()


class TourRetrieveView(RetrieveModelMixin, GenericViewSet):
    queryset = models.Tour.objects.order_by('-id')
    serializer_class = TourDetailSerializer

    def get_queryset(self):
        return models.Tour.objects.select_related('country').prefetch_related(
            'reviews',
            'advantages',
            'formats',
            'prices',
            Prefetch(
                'images',
                queryset=models.TourImage.objects.order_by('position')
            ),
            Prefetch(
                'dates',
                queryset=models.TourDate.objects.order_by('start_date')
            ),
            Prefetch(
                'programs',
                queryset=models.TourProgram.objects.order_by(
                    'day'
                ).select_related(
                    'accommodation'
                ).prefetch_related('images')
            )
        ).distinct()


class TourSeasonListView(ListModelMixin, GenericViewSet):
    serializer_class = TourSeasonSerializer
    queryset = models.TourSeason.objects.order_by('id')


class TourPlacementListView(ListModelMixin, GenericViewSet):
    serializer_class = TourPlacementSerializer
    queryset = models.TourPlacement.objects.order_by('id')


class TourFormatListView(ListModelMixin, GenericViewSet):
    serializer_class = TourFormatSerializer
    queryset = models.TourFormat.objects.order_by('id')


class TourFilterDataAPI(APIView):

    def get(self, request):
        min_price = None
        max_price = None
        min_date = None
        max_date = None

        tour_price_min = TourPrice.objects.order_by('price').first()
        tour_price_max = TourPrice.objects.order_by('-price').first()

        tour_date_min = Tour.objects.order_by('duration').first()
        tour_date_max = Tour.objects.order_by('-duration').first()

        if tour_price_max and tour_price_min:
            min_price = tour_price_min.price
            max_price = tour_price_max.price

        if tour_date_min and tour_date_max:
            min_date = tour_date_min.duration
            max_date = tour_date_max.duration

        result = {
            'min_price': min_price,
            'max_price': max_price,
            'min_date': min_date,
            'max_date': max_date
        }

        return Response(result)
