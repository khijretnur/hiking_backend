from django.contrib import admin
from tags.models import Tag
from modeltranslation.admin import TabbedTranslationAdmin

#
# @admin.register(Tag)
# class TagAdmin(TabbedTranslationAdmin):
#     list_display = ('id', 'name')
