from modeltranslation.translator import TranslationOptions, register
from recommendations import models


@register(models.RecommendationCategory)
class RecommendationCategoryTranslationOption(TranslationOptions):
    fields = ('title',)


@register(models.Recommendation)
class RecommendationTranslationOption(TranslationOptions):
    fields = ('title', 'text', 'description', 'inside_text')

