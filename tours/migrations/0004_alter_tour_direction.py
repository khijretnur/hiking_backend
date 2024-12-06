# Generated by Django 4.2.4 on 2023-09-20 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tours', '0003_tour_must_know'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tour',
            name='direction',
            field=models.PositiveIntegerField(choices=[(1, 'Внутри Казахстана'), (2, 'Зарубежные')], verbose_name='Направление'),
        ),
    ]