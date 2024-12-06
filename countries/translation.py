from modeltranslation.translator import register, TranslationOptions
from countries import models


@register(models.Country)
class CountryTranslationOption(TranslationOptions):
    fields = ('name',)

