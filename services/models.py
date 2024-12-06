from django.db import models
from utils.models import BaseModel
from ckeditor.fields import RichTextField


class Service(BaseModel):
    name = models.CharField(max_length=255, verbose_name='Название услуги')
    image = models.ImageField(upload_to='services/', verbose_name='Фото')
    detail_image = models.ImageField(upload_to='services/', verbose_name='Внутренее фото', null=True)
    text = RichTextField(verbose_name='Текст')
    description = models.CharField(max_length=255, null=True, verbose_name='Краткое описание')
    position = models.PositiveIntegerField(verbose_name='Позиция')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'


class ServiceImage(BaseModel):
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='images', verbose_name='Сервис')
    image = models.ImageField(upload_to='services/', verbose_name='Внутренее фото')
    position = models.PositiveIntegerField(verbose_name='Позиция')

    def __str__(self):
        return f'Фото к сервису "{self.service}"'

    class Meta:
        verbose_name = 'Фото услуги'
        verbose_name_plural = 'Фотографии услуг'
