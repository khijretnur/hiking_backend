# Generated by Django 4.2.4 on 2023-12-14 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advantages', '0004_touradvantage_text_en_touradvantage_text_kk_and_more'),
        ('tours', '0015_mustknow_remove_tour_must_know_en_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tour',
            name='advantages',
            field=models.ManyToManyField(to='advantages.touradvantage', verbose_name='Преимущества тура'),
        ),
    ]
