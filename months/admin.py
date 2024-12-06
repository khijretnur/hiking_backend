from django.contrib import admin
from months.models import Month


@admin.register(Month)
class MonthAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'month_num', 'season')

    search_fields = ('name',)

    list_filter = ('season',)
