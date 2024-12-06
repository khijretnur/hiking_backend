from modeltranslation.translator import register, TranslationOptions
from documents import models


@register(models.Document)
class DocumentTranslationOption(TranslationOptions):
    fields = ('title',)
