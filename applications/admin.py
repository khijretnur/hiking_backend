from django.contrib import admin
from applications.models import Application


@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'phone_number', 'email')
    list_display_links = ('id', 'full_name')

    search_fields = ('full_name', 'phone_number')
