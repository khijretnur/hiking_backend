from django.db import models
from utils.models import BaseModel


class Tag(BaseModel):
    name = models.CharField(max_length=255, verbose_name='Имя тэга')
    position = models.PositiveIntegerField(verbose_name='Позиция')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тэг'
        verbose_name_plural = 'Тэги'
