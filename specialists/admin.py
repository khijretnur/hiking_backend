from django.contrib import admin
from specialists.models import Specialist
from modeltranslation.admin import TabbedTranslationAdmin


@admin.register(Specialist)
class SpecialistAdmin(TabbedTranslationAdmin):
    list_display = ('id', 'full_name', 'experience')
    list_display_links = ('id', 'full_name')

    search_fields = ('full_name',)
