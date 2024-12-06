# Generated by Django 4.2.4 on 2023-10-27 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='author_en',
            field=models.CharField(max_length=255, null=True, verbose_name='Имя автора'),
        ),
        migrations.AddField(
            model_name='review',
            name='author_kk',
            field=models.CharField(max_length=255, null=True, verbose_name='Имя автора'),
        ),
        migrations.AddField(
            model_name='review',
            name='author_ru',
            field=models.CharField(max_length=255, null=True, verbose_name='Имя автора'),
        ),
        migrations.AddField(
            model_name='review',
            name='text_en',
            field=models.TextField(null=True, verbose_name='Текст'),
        ),
        migrations.AddField(
            model_name='review',
            name='text_kk',
            field=models.TextField(null=True, verbose_name='Текст'),
        ),
        migrations.AddField(
            model_name='review',
            name='text_ru',
            field=models.TextField(null=True, verbose_name='Текст'),
        ),
    ]
