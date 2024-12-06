from django.db import models


class Advantage(models.Model):
    icon = models.ImageField(verbose_name='Иконка', upload_to='advantage_icons/')
    title = models.CharField(max_length=150, verbose_name='Заголовок')
    text = models.CharField(max_length=250, verbose_name='Текст')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Преимущество'
        verbose_name_plural = 'Преимущества'


class TourAdvantage(models.Model):
    title = models.CharField(max_length=150, verbose_name='Заголовок')
    text = models.CharField(max_length=250, verbose_name='Текст')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Преимущество тура'
        verbose_name_plural = 'Преимущества тура'
