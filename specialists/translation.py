from modeltranslation.translator import TranslationOptions, register
from specialists import models


@register(models.Specialist)
class SpecialistTranslationOption(TranslationOptions):
    fields = ('full_name', 'description')
