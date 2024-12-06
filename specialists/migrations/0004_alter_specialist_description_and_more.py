# Generated by Django 4.2.4 on 2023-11-09 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('specialists', '0003_alter_specialist_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='specialist',
            name='description',
            field=models.TextField(verbose_name='Описание специалиста'),
        ),
        migrations.AlterField(
            model_name='specialist',
            name='description_en',
            field=models.TextField(null=True, verbose_name='Описание специалиста'),
        ),
        migrations.AlterField(
            model_name='specialist',
            name='description_kk',
            field=models.TextField(null=True, verbose_name='Описание специалиста'),
        ),
        migrations.AlterField(
            model_name='specialist',
            name='description_ru',
            field=models.TextField(null=True, verbose_name='Описание специалиста'),
        ),
    ]
