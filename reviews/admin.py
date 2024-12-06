from django.contrib import admin
from reviews.models import Review


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'tour')
    list_display_links = ('id', 'author')

    list_filter = ('tour',)
