# Generated by Django 4.2.4 on 2023-09-18 14:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tours', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tour',
            old_name='city',
            new_name='country',
        ),
    ]
