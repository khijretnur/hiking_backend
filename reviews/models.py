from django.db import models
from utils.models import BaseModel


class Review(BaseModel):
    tour = models.ForeignKey(
        'tours.Tour',
        on_delete=models.CASCADE,
        related_name='reviews',
        verbose_name='Тур'
    )
    author = models.CharField(
        max_length=255,
        verbose_name='Имя автора'
    )
    author_age = models.CharField(
        max_length=3,
        verbose_name='Возраст автора'
    )
    image = models.ImageField(verbose_name='Фото', null=True, upload_to='reviews/')
    text = models.TextField(verbose_name='Текст')

    def __str__(self):
        return f'Отзыв от {self.author} на тур: "{self.tour}"'

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
