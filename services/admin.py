from django.contrib import admin
from services.models import Service, ServiceImage
from modeltranslation.admin import TabbedTranslationAdmin


class ServiceImageTabular(admin.TabularInline):
    model = ServiceImage
    extra = 3
    max_num = 3


@admin.register(ServiceImage)
class ServiceImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'service', 'image')

    list_filter = ('service',)


@admin.register(Service)
class ServiceAdmin(TabbedTranslationAdmin):
    list_display = ('id', 'name', 'position')
    list_display_links = ('id', 'name')

    search_fields = ('name',)

    inlines = (ServiceImageTabular,)
