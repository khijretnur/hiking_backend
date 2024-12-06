from django.db import models
from utils.models import BaseModel


class Country(BaseModel):
    name = models.CharField(max_length=255, verbose_name='Страна')
    image = models.ImageField(verbose_name='Картинка', null=True, blank=True)
    position = models.PositiveIntegerField(null=True, blank=True, verbose_name='Позиция')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Страна'
        verbose_name_plural = 'Страны'
