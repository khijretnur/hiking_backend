from django.contrib import admin
from banners.models import Banner


@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ('id', 'image', 'position')
    list_display_links = ('id', 'image')
