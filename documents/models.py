from django.db import models


class Document(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название документа')
    file = models.FileField(upload_to='documents/', null=True)
    position = models.PositiveIntegerField(verbose_name='Позиция')
    file_type = models.CharField(max_length=50, null=True, blank=True, verbose_name='Тип файла', help_text='Заполнится сам')

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.file_type and self.file:
            # Extract file type from the file name, assuming it's in the format "filename.extension"
            file_type = self.file.name.split('.')[-1].lower()
            self.file_type = file_type

        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Документ'
        verbose_name_plural = 'Документы'


class PrivacyStatement(models.Model):
    file = models.FileField(verbose_name='Файл "Положение о конфиденциальности"', upload_to='privacy_statements/')

    class Meta:
        verbose_name = 'Положение о конфиденциальности'
        verbose_name_plural = 'Положения о конфиденциальности'
