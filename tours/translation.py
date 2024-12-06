from modeltranslation.translator import register, TranslationOptions
from tours import models


@register(models.Accommodation)
class AccommodationTranslationOption(TranslationOptions):
    fields = ('title', 'text')


@register(models.MustKnow)
class MustKnowTranslationOption(TranslationOptions):
    fields = ('title', 'text')


@register(models.TourFormat)
class TourFormatTranslationOption(TranslationOptions):
    fields = ('name',)


@register(models.TourSeason)
class TourSeasonTranslationOption(TranslationOptions):
    fields = ('name',)


@register(models.TourPlacement)
class TourPlacementTranslationOption(TranslationOptions):
    fields = ('name',)


@register(models.Tour)
class TourTranslationOption(TranslationOptions):
    fields = ('name', 'short_description', 'description', 'route', 'main_image_text', 'included_things')


@register(models.TourPrice)
class TourPriceTranslationOption(TranslationOptions):
    fields = ('text',)


@register(models.TourProgram)
class TourProgramTranslationOption(TranslationOptions):
    fields = ('title', 'description', 'route', 'food')


