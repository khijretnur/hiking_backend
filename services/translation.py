from modeltranslation.translator import TranslationOptions, register
from services import models


@register(models.Service)
class ServiceTranslationOption(TranslationOptions):
    fields = ('name', 'text', 'description')
