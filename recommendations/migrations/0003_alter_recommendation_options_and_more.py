# Generated by Django 4.2.4 on 2023-11-09 08:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recommendations', '0002_recommendation_text_en_recommendation_text_kk_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='recommendation',
            options={'verbose_name': 'Рекоммендация', 'verbose_name_plural': 'Рекоммендации'},
        ),
        migrations.AlterModelOptions(
            name='recommendationcategory',
            options={'verbose_name': 'Категория рекоммендаций', 'verbose_name_plural': 'Категория рекоммендации'},
        ),
        migrations.AlterModelOptions(
            name='recommendationfile',
            options={'verbose_name': 'Файл рекоммендаций', 'verbose_name_plural': 'Файлы рекомендации'},
        ),
    ]
