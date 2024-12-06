from django.contrib import admin
from tours import models
from modeltranslation.admin import TabbedTranslationAdmin


class TourImageTabular(admin.TabularInline):
    model = models.TourImage
    extra = 3


class TourPriceTabular(admin.TabularInline):
    model = models.TourPrice
    extra = 1


class TourDateTabular(admin.TabularInline):
    model = models.TourDate
    extra = 3


class AccommodationImageTabular(admin.TabularInline):
    model = models.AccommodationImage
    extra = 3


@admin.register(models.AccommodationImage)
class AccommodationImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'accommodation')
    list_display_links = ('id', 'accommodation')

    list_filter = ('accommodation',)


@admin.register(models.Accommodation)
class AccommodationAdmin(TabbedTranslationAdmin):
    list_display = ('id', 'title_ru')
    list_display_links = ('id', 'title_ru')

    search_fields = ('title_ru',)

    inlines = (AccommodationImageTabular,)


@admin.register(models.MustKnow)
class MustKnowAdmin(TabbedTranslationAdmin):
    list_display = ('id', 'title_ru')
    list_display_links = ('id', 'title_ru')

    search_fields = ('title_ru',)


@admin.register(models.TourSeason)
class TourSeasonAdmin(TabbedTranslationAdmin):
    list_display = ('id', 'name_ru')

    search_fields = ('name_ru',)


@admin.register(models.TourFormat)
class TourFormatAdmin(TabbedTranslationAdmin):
    list_display = ('id', 'name_ru')

    search_fields = ('name_ru',)


@admin.register(models.TourPlacement)
class TourPlacementAdmin(TabbedTranslationAdmin):
    list_display = ('id', 'name_ru')

    search_fields = ('name_ru',)


@admin.register(models.TourImage)
class TourImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'tour', 'position', 'image_tag')
    list_display_links = ('id', 'tour')

    list_filter = ('tour',)


@admin.register(models.TourPrice)
class TourPriceAdmin(TabbedTranslationAdmin):
    list_display = ('id', 'tour', 'price', 'currency')
    list_display_links = ('id', 'tour')

    list_filter = ('tour',)


@admin.register(models.TourDate)
class TourDateAdmin(admin.ModelAdmin):
    list_display = ('id', 'tour', 'start_date', 'end_date')
    list_display_links = ('id', 'tour')

    list_filter = ('tour',)


@admin.register(models.Tour)
class TourAdmin(TabbedTranslationAdmin):
    list_display = ('id', 'name_ru', 'country')
    list_display_links = ('id', 'name_ru')

    search_fields = ('name',)

    filter_horizontal = ['advantages', 'seasons', 'placements', 'formats', 'must_know']

    inlines = (TourImageTabular, TourPriceTabular, TourDateTabular)


class TourProgramImageTabular(admin.TabularInline):
    model = models.TourProgramImage
    extra = 3


@admin.register(models.TourProgram)
class TourProgramAdmin(TabbedTranslationAdmin):
    list_display = ('id', 'tour', 'day', 'title')
    list_display_links = ('id', 'tour')

    list_filter = ('tour',)

    inlines = (TourProgramImageTabular,)


@admin.register(models.TourProgramImage)
class TourProgramImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'tour_program', 'image_tag')

    list_filter = ('tour_program',)
