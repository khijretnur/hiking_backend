# Generated by Django 4.2.4 on 2023-11-09 08:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0002_review_author_en_review_author_kk_review_author_ru_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='review',
            options={'verbose_name': 'Отзыв', 'verbose_name_plural': 'Отзывы'},
        ),
    ]
