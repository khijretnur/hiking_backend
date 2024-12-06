from modeltranslation.translator import TranslationOptions, register
from reviews import models


@register(models.Review)
class ReviewTranslationOption(TranslationOptions):
    fields = ('author', 'text')
