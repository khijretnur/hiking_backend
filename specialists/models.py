from django.db import models


class Specialist(models.Model):
    full_name = models.CharField(max_length=255, verbose_name='Полное имя')
    experience = models.PositiveIntegerField(verbose_name='Опыт работы')
    description = models.TextField(verbose_name='Описание специалиста')
    image = models.ImageField(upload_to='specialists/', verbose_name='Фото специалиста')

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = 'Специалист'
        verbose_name_plural = 'Специалисты'
