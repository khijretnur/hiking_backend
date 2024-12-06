# Generated by Django 4.2.4 on 2023-09-02 18:48

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tags', '0001_initial'),
        ('countries', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tour',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=255, verbose_name='Название тура')),
                ('main_image', models.ImageField(upload_to='tour_mains/', verbose_name='Главное фото')),
                ('short_description', models.TextField(verbose_name='Краткое описание тура')),
                ('description', ckeditor.fields.RichTextField(verbose_name='Полное описание тура')),
                ('route', models.TextField(verbose_name='Маршрут тура')),
                ('direction', models.PositiveIntegerField(choices=[(1, 'Внутри Казахстана'), (2, 'Зарубежные')])),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tours', to='countries.country', verbose_name='Страна')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TourFormat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(help_text='Например "Городские туры"', max_length=255, verbose_name='Название формата тура')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TourPlacement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(help_text='Например "Отели"', max_length=255, verbose_name='Тип размещения')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TourProgram',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('day', models.PositiveIntegerField(verbose_name='День тура')),
                ('description', models.TextField(verbose_name='Описание дня')),
                ('route', models.CharField(max_length=255, verbose_name='Маршрут программы')),
                ('food', models.CharField(max_length=255, verbose_name='Еда маршрута')),
                ('tour', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='programs', to='tours.tour', verbose_name='Тур')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TourSeason',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(help_text='Например "Осень"', max_length=255, verbose_name='Сезон')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TourProgramImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('image', models.ImageField(upload_to='tour_program/', verbose_name='Картинка')),
                ('tour_program', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='tours.tourprogram', verbose_name='Программа тура')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TourPrice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('price', models.PositiveIntegerField(verbose_name='Цена')),
                ('currency', models.CharField(default='₽', max_length=10, verbose_name='Валюта')),
                ('text', models.TextField(verbose_name='Информация о стоимости')),
                ('tour', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='prices', to='tours.tour', verbose_name='Тур')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TourImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('image', models.ImageField(upload_to='tours/', verbose_name='Картинка')),
                ('position', models.PositiveIntegerField(verbose_name='Позиция')),
                ('tour', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='tours.tour', verbose_name='Тур')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TourDate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('start_date', models.DateField(verbose_name='Дата начала тура')),
                ('end_date', models.DateField(verbose_name='Дата конца тура')),
                ('tour', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dates', to='tours.tour', verbose_name='Тур')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='tour',
            name='formats',
            field=models.ManyToManyField(to='tours.tourformat', verbose_name='Форматы'),
        ),
        migrations.AddField(
            model_name='tour',
            name='placements',
            field=models.ManyToManyField(to='tours.tourplacement', verbose_name='Типы размещения'),
        ),
        migrations.AddField(
            model_name='tour',
            name='seasons',
            field=models.ManyToManyField(to='tours.tourseason', verbose_name='Сезоны'),
        ),
        migrations.AddField(
            model_name='tour',
            name='tags',
            field=models.ManyToManyField(to='tags.tag', verbose_name='Тэги'),
        ),
    ]