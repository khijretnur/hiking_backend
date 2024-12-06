from django.db import models
from django.utils.html import format_html

from utils.models import BaseModel
from ckeditor.fields import RichTextField


class TourFormat(BaseModel):
    name = models.CharField(max_length=255, verbose_name='Название формата тура', help_text='Например "Городские туры"')
    image = models.ImageField(upload_to='tour_formats/', verbose_name='Фото формата тура', null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Формат'
        verbose_name_plural = 'Форматы'


class TourSeason(BaseModel):
    name = models.CharField(max_length=255, verbose_name='Сезон', help_text='Например "Осень"')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Сезон'
        verbose_name_plural = 'Сезоны'


class TourPlacement(BaseModel):
    name = models.CharField(max_length=255, verbose_name='Тип размещения', help_text='Например "Отели"')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тип размещения'
        verbose_name_plural = 'Типы размещении'


class MustKnow(BaseModel):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    text = models.TextField(verbose_name='Текст')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Важно знать'
        verbose_name_plural = 'Важно знать'


class Tour(BaseModel):
    name = models.CharField(max_length=255, verbose_name='Название тура')
    main_image = models.ImageField(upload_to='tour_mains/', verbose_name='Главное фото')
    main_image_text = RichTextField(verbose_name='Текст на главном фото', null=True)
    duration = models.PositiveIntegerField(null=True, blank=True, verbose_name='Продолжительность', help_text='Для фильтра')
    distance = models.PositiveIntegerField(null=True, verbose_name='Дистанция (в км)')
    budget = models.PositiveIntegerField(null=True, blank=True, verbose_name='Бюджет', help_text='Для фильтра')
    short_description = models.TextField(verbose_name='Краткое описание тура')
    description = RichTextField(verbose_name='Полное описание тура')
    advantages = models.ManyToManyField('advantages.TourAdvantage', verbose_name='Преимущества тура')
    route = models.TextField(verbose_name='Маршрут тура')
    country = models.ForeignKey('countries.Country', on_delete=models.CASCADE, related_name='tours', verbose_name='Страна')
    seasons = models.ManyToManyField(TourSeason, verbose_name='Сезоны')
    placements = models.ManyToManyField(TourPlacement, verbose_name='Типы размещения')
    formats = models.ManyToManyField(TourFormat, verbose_name='Форматы')
    must_know = models.ManyToManyField(MustKnow, verbose_name='Важно знать')
    days = models.PositiveIntegerField(null=True, verbose_name='Количство дней')
    nights = models.PositiveIntegerField(null=True, verbose_name='Количество ночей')
    included_things = RichTextField(
        verbose_name='Включено/Не включено',
        null=True,
        help_text='Информация о том что включено/не включено в стоимость тура'
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тур'
        verbose_name_plural = 'Туры'


class TourImage(BaseModel):
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE, related_name='images', verbose_name='Тур')
    image = models.ImageField(upload_to='tours/', verbose_name='Картинка')
    position = models.PositiveIntegerField(verbose_name='Позиция')

    def image_tag(self):
        return format_html('<img src="{}" width="75" height="50" />', self.image.url)

    def __str__(self):
        return f'Картинка к {self.tour}'

    class Meta:
        verbose_name = 'Картинка тура'
        verbose_name_plural = 'Картинки туров'


class TourPrice(BaseModel):
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE, related_name='prices', verbose_name='Тур')
    price = models.PositiveIntegerField(verbose_name='Цена')
    currency = models.CharField(max_length=10, verbose_name='Валюта', default='₽')
    discount_till_date = models.DateField(null=True, blank=True, verbose_name='Скидка до')
    text = models.TextField(verbose_name='Информация о стоимости')

    def __str__(self):
        return f'{self.tour} - {self.price} {self.currency}'

    class Meta:
        verbose_name = 'Цена тура'
        verbose_name_plural = 'Цены туров'


class Accommodation(BaseModel):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    text = models.TextField(verbose_name='Текст')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '"Проживание" программы тура'
        verbose_name_plural = '"Проживания" программы туров'


class AccommodationImage(BaseModel):
    accommodation = models.ForeignKey(
        Accommodation,
        on_delete=models.CASCADE,
        related_name='images',
        verbose_name='Проживание'
    )
    image = models.ImageField(verbose_name='Фото "Проживания"')

    def __str__(self):
        return f'Фото к проживанию в: {self.accommodation}'

    class Meta:
        verbose_name = 'Фото "проживания"'
        verbose_name_plural = 'Фотографии "проживании"'


class TourProgram(BaseModel):
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE, related_name='programs', verbose_name='Тур')
    day = models.PositiveIntegerField(verbose_name='День тура')
    title = models.CharField(max_length=255, verbose_name='Заголовок', null=True)
    description = models.TextField(verbose_name='Описание дня')
    route = models.CharField(max_length=255, verbose_name='Маршрут программы')
    food = models.CharField(max_length=255, verbose_name='Еда маршрута')
    accommodation = models.ForeignKey(
        Accommodation,
        on_delete=models.SET_NULL,
        verbose_name='Проживание',
        related_name='tour_programs',
        null=True,
        blank=True
    )

    def __str__(self):
        return f'День "{self.day}" тура "{self.tour}"'

    class Meta:
        verbose_name = 'Программа тура'
        verbose_name_plural = 'Программы туров'


class TourProgramImage(BaseModel):
    tour_program = models.ForeignKey(
        TourProgram,
        on_delete=models.CASCADE,
        related_name='images',
        verbose_name='Программа тура'
    )
    image = models.ImageField(upload_to='tour_program/', verbose_name='Картинка')

    def image_tag(self):
        return format_html('<img src="{}" width="75" height="50" />', self.image.url)

    def __str__(self):
        return f'Картинка к {self.tour_program}'

    class Meta:
        verbose_name = 'Фото программы тура'
        verbose_name_plural = 'Фотографии программ туров'


class TourDate(BaseModel):
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE, related_name='dates', verbose_name='Тур')
    start_date = models.DateField(verbose_name='Дата начала тура')
    end_date = models.DateField(verbose_name='Дата конца тура')

    def __str__(self):
        return f'{self.tour} "{self.start_date} - {self.end_date}"'

    class Meta:
        verbose_name = 'Даты тура'
        verbose_name_plural = 'Даты туров'
