# Generated by Django 4.2.4 on 2023-12-14 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advantages', '0003_touradvantage'),
    ]

    operations = [
        migrations.AddField(
            model_name='touradvantage',
            name='text_en',
            field=models.CharField(max_length=250, null=True, verbose_name='Текст'),
        ),
        migrations.AddField(
            model_name='touradvantage',
            name='text_kk',
            field=models.CharField(max_length=250, null=True, verbose_name='Текст'),
        ),
        migrations.AddField(
            model_name='touradvantage',
            name='text_ru',
            field=models.CharField(max_length=250, null=True, verbose_name='Текст'),
        ),
        migrations.AddField(
            model_name='touradvantage',
            name='title_en',
            field=models.CharField(max_length=150, null=True, verbose_name='Заголовок'),
        ),
        migrations.AddField(
            model_name='touradvantage',
            name='title_kk',
            field=models.CharField(max_length=150, null=True, verbose_name='Заголовок'),
        ),
        migrations.AddField(
            model_name='touradvantage',
            name='title_ru',
            field=models.CharField(max_length=150, null=True, verbose_name='Заголовок'),
        ),
    ]