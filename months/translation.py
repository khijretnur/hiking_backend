from modeltranslation.translator import TranslationOptions, register
from months import models


@register(models.Month)
class MonthTranslationOption(TranslationOptions):
    fields = ('name',)
