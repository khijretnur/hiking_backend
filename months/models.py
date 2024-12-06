from django.db import models


class Month(models.Model):
    name = models.CharField(max_length=155, verbose_name='Название месяца')
    month_num = models.PositiveIntegerField(verbose_name='Номер месяца')
    season = models.ForeignKey('tours.TourSeason', on_delete=models.SET_NULL, null=True, verbose_name='Сезон')

    class Meta:
        verbose_name = 'Месяц'
        verbose_name_plural = 'Месяцы'
