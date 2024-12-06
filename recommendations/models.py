from django.db import models
from utils.models import BaseModel
from ckeditor.fields import RichTextField


class RecommendationCategory(BaseModel):
    title = models.CharField(max_length=255, verbose_name='Тип рекоммендации')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория рекоммендаций'
        verbose_name_plural = 'Категория рекоммендации'


class Recommendation(BaseModel):
    category = models.ForeignKey(
        RecommendationCategory,
        on_delete=models.CASCADE,
        related_name='recommendations',
        verbose_name='Категория'
    )
    title = models.CharField(max_length=255, verbose_name='Рекоммендация')
    text = RichTextField(verbose_name='Текст рекоммендации')
    description = models.CharField(max_length=255, verbose_name='Описание рекоммендации', null=True)
    detail_image = models.ImageField(verbose_name='Внутренее фото', null=True)
    inside_text = models.CharField(max_length=255, verbose_name='Внутренни текст', null=True)
    image = models.ImageField(verbose_name='Картинка рекоммендации')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Рекоммендация'
        verbose_name_plural = 'Рекоммендации'


class RecommendationFile(BaseModel):
    recommendation = models.ForeignKey(
        Recommendation,
        on_delete=models.CASCADE,
        related_name='files',
        verbose_name='Рекоммендация'
    )
    file = models.FileField(verbose_name='Файл')
    position = models.PositiveIntegerField(verbose_name='Позиция файла')

    def __str__(self):
        return f'Файл к рекомендации "{self.recommendation}"'

    class Meta:
        verbose_name = 'Файл рекоммендаций'
        verbose_name_plural = 'Файлы рекомендации'
