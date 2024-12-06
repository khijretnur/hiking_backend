from modeltranslation.translator import register, TranslationOptions
from advantages import models


@register(models.Advantage)
class AdvantageTranslationOption(TranslationOptions):
    fields = ('title', 'text')


@register(models.TourAdvantage)
class TourAdvantageTranslationOption(TranslationOptions):
    fields = ('title', 'text')
