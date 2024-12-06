from django.contrib import admin
from advantages import models
from modeltranslation.admin import TabbedTranslationAdmin


@admin.register(models.Advantage)
class AdvantageAdmin(TabbedTranslationAdmin):
    list_display = ('id', 'title_ru')
    list_display_links = ('id', 'title_ru')


@admin.register(models.TourAdvantage)
class TourAdvantageAdmin(TabbedTranslationAdmin):
    list_display = ('id', 'title_ru')
    list_display_links = ('id', 'title_ru')
