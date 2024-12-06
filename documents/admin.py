from django.contrib import admin

from documents.forms import PrivacyStatementAdminForm
from documents.models import Document, PrivacyStatement
from modeltranslation.admin import TabbedTranslationAdmin


@admin.register(Document)
class DocumentAdmin(TabbedTranslationAdmin):
    list_display = ('id', 'title')

#
# @admin.register(PrivacyStatement)
# class PrivacyStatementAdmin(admin.ModelAdmin):
#     list_display = ('id', 'file')
#     form = PrivacyStatementAdminForm
