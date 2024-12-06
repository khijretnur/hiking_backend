from rest_framework import serializers
from tours import models


class TourReviewSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    author = serializers.CharField()
    author_age = serializers.CharField()
    text = serializers.CharField()
    image = serializers.ImageField()


class TourAdvantageSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField()
    text = serializers.CharField()


class MustKnowSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField()
    text = serializers.CharField()


class TourCountrySerializer(serializers.Serializer):
    name = serializers.CharField()


class TourTagSerializer(serializers.Serializer):
    name = serializers.CharField()


class TourImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.TourImage
        fields = ('image',)


class TourSeasonSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.TourSeason
        fields = ('id', 'name',)


class TourPlacementSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.TourPlacement
        fields = ('id', 'name',)


class TourFormatSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.TourFormat
        fields = ('id', 'name', 'image')


class TourPriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.TourPrice
        fields = ('price', 'currency', 'text', 'discount_till_date')


class TourProgramImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.TourProgramImage
        fields = ('image',)


class AccommodationImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.AccommodationImage
        fields = ('image',)


class AccommodationSerializer(serializers.ModelSerializer):
    images = AccommodationImageSerializer(many=True)

    class Meta:
        model = models.Accommodation
        fields = ('id', 'title', 'text', 'images')


class TourProgramSerializer(serializers.ModelSerializer):
    images = TourProgramImageSerializer(many=True)
    accommodation = AccommodationSerializer()

    class Meta:
        model = models.TourProgram
        fields = ('day', 'description', 'title', 'route', 'food', 'images', 'accommodation')


class TourDateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.TourDate
        fields = ('start_date', 'end_date')


class TourSerializer(serializers.ModelSerializer):
    images = TourImageSerializer(many=True)
    country = TourCountrySerializer()
    lowest_price = serializers.SerializerMethodField()
    earliest_date = serializers.SerializerMethodField()
    latest_date = serializers.SerializerMethodField()
    formats = TourFormatSerializer(many=True)
    dates = TourDateSerializer(many=True)

    class Meta:
        model = models.Tour
        exclude = (
            'main_image', 'description', 'seasons', 'placements',
            'created_at', 'updated_at', 'duration',
            'budget', 'name_kk', 'name_en', 'name_ru', 'must_know',
            'short_description_ru', 'short_description_kk',
            'short_description_en',
            'route_kk',
            'route_ru',
            'route_en',
            'description_kk',
            'description_en',
            'description_ru',
            'included_things_ru',
            'included_things_kk',
            'included_things_en',
            'main_image_text_ru',
            'main_image_text_kk',
            'main_image_text_en'
        )

    def get_lowest_price(self, obj):
        lowest_price_obj = obj.prices.order_by('price').first()
        if lowest_price_obj:
            return f'{lowest_price_obj.price} {lowest_price_obj.currency}'
        return None

    def get_earliest_date(self, obj):
        earliest_date_obj = obj.dates.order_by('start_date').first()
        if earliest_date_obj:
            return earliest_date_obj.start_date
        return None

    def get_latest_date(self, obj):
        latest_date_obj = obj.dates.order_by('-end_date').first()
        if latest_date_obj:
            return latest_date_obj.end_date
        return None


class TourDetailSerializer(serializers.ModelSerializer):
    images = TourImageSerializer(many=True)
    prices = TourPriceSerializer(many=True)
    programs = TourProgramSerializer(many=True)
    dates = TourDateSerializer(many=True)
    formats = TourFormatSerializer(many=True)
    reviews = TourReviewSerializer(many=True)
    advantages = TourAdvantageSerializer(many=True)
    must_know = MustKnowSerializer(many=True)
    country = TourCountrySerializer()

    class Meta:
        model = models.Tour
        exclude = ('seasons', 'placements',
                   'created_at', 'updated_at',
                   'short_description', 'duration', 'budget',
                   'name_kk', 'name_en', 'name_ru',
                   'short_description_kk',
                   'short_description_ru',
                   'short_description_en',
                   'route_kk',
                   'route_ru',
                   'route_en',
                   'description_kk',
                   'description_en',
                   'description_ru',
                   'included_things_ru',
                   'included_things_kk',
                   'included_things_en',
                   'main_image_text_ru',
                   'main_image_text_kk',
                   'main_image_text_en'
                   )
