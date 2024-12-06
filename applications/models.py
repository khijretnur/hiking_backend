from django.db import models
from utils.models import BaseModel


class Application(BaseModel):
    full_name = models.CharField(max_length=100, verbose_name='Имя')
    phone_number = models.CharField(max_length=30, verbose_name='Номер телефона')
    email = models.EmailField(verbose_name='Почта')
    comment = models.CharField(max_length=255, verbose_name='Комментарий')

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'
