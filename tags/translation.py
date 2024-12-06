from modeltranslation.translator import register, TranslationOptions
from tags import models


@register(models.Tag)
class TagTranslatedOption(TranslationOptions):
    fields = ('name',)
