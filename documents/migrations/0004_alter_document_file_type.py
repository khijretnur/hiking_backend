# Generated by Django 4.2.4 on 2023-12-12 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0003_remove_document_text_remove_document_text_en_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='file_type',
            field=models.CharField(blank=True, help_text='Заполнится сам', max_length=50, null=True, verbose_name='Тип файла'),
        ),
    ]