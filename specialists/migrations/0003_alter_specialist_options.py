# Generated by Django 4.2.4 on 2023-11-09 08:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('specialists', '0002_specialist_description_en_specialist_description_kk_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='specialist',
            options={'verbose_name': 'Специалист', 'verbose_name_plural': 'Специалисты'},
        ),
    ]