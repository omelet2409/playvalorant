# Generated by Django 4.1.7 on 2023-03-23 05:39

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_remove_map_map_description_remove_map_map_img_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Weapon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=500)),
                ('img', cloudinary.models.CloudinaryField(max_length=255, verbose_name='img')),
                ('slug', models.SlugField()),
                ('weapon_detail', models.CharField(max_length=500)),
            ],
            options={
                'verbose_name': 'weapon',
                'verbose_name_plural': 'weapons',
            },
        ),
    ]
