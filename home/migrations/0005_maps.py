# Generated by Django 4.1.7 on 2023-03-23 04:34

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_alter_agent_skill_c_video_alter_agent_skill_e_video_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Maps',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=500)),
                ('img', cloudinary.models.CloudinaryField(max_length=255, verbose_name='img')),
                ('slug', models.SlugField()),
                ('map_name', models.CharField(max_length=50)),
                ('map_img', cloudinary.models.CloudinaryField(max_length=255, verbose_name='icon')),
                ('map_location', models.CharField(max_length=250)),
                ('map_description', models.CharField(max_length=250)),
            ],
            options={
                'verbose_name': 'map',
                'verbose_name_plural': 'maps',
            },
        ),
    ]