from django.contrib import admin
from countries.models import Country
from modeltranslation.admin import TabbedTranslationAdmin


@admin.register(Country)
class CountryAdmin(TabbedTranslationAdmin):
    list_display = ('id', 'name_ru')
    list_display_links = ('id', 'name_ru')

    search_fields = ('name_ru',)
