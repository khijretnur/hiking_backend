from django.contrib import admin
from recommendations import models
from modeltranslation.admin import TabbedTranslationAdmin


class RecommendationFileTabular(admin.TabularInline):
    model = models.RecommendationFile
    extra = 3
    max_num = 3


@admin.register(models.RecommendationCategory)
class RecommendationCategoryAdmin(TabbedTranslationAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')

    search_fields = ('title',)


@admin.register(models.Recommendation)
class RecommendationAdmin(TabbedTranslationAdmin):
    list_display = ('id', 'title', 'category')
    list_display_links = ('id', 'title')

    inlines = (RecommendationFileTabular,)

    search_fields = ('title',)

    list_filter = ('category',)


@admin.register(models.RecommendationFile)
class RecommendationFileAdmin(admin.ModelAdmin):
    list_display = ('id', 'recommendation')
    list_display_links = ('id', 'recommendation')

    list_filter = ('recommendation',)

