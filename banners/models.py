from django.db import models


class Banner(models.Model):
    image = models.ImageField(upload_to='banners/', verbose_name='Фото баннера')
    mobile_image = models.ImageField(upload_to='banners_mobile/', verbose_name='Фото баннера (для мобильной версии)')
    position = models.PositiveIntegerField(verbose_name='Позиция фото')

    def __str__(self):
        return f'Баннер с id: {self.id}'

    class Meta:
        verbose_name = 'Баннер'
        verbose_name_plural = 'Баннеры'
