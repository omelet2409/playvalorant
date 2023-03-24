# Generated by Django 4.1.7 on 2023-03-23 02:08

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Agent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=500)),
                ('img', cloudinary.models.CloudinaryField(max_length=255, verbose_name='img')),
                ('skill_q_name', models.CharField(max_length=50)),
                ('skill_q_icon', cloudinary.models.CloudinaryField(max_length=255, verbose_name='icon')),
                ('skill_q_video', cloudinary.models.CloudinaryField(max_length=255, verbose_name='video')),
                ('skill_q_description', models.CharField(max_length=250)),
                ('skill_e_name', models.CharField(max_length=50)),
                ('skill_e_icon', cloudinary.models.CloudinaryField(max_length=255, verbose_name='icon')),
                ('skill_e_video', cloudinary.models.CloudinaryField(max_length=255, verbose_name='video')),
                ('skill_e_description', models.CharField(max_length=250)),
                ('skill_c_name', models.CharField(max_length=50)),
                ('skill_c_icon', cloudinary.models.CloudinaryField(max_length=255, verbose_name='icon')),
                ('skill_c_video', cloudinary.models.CloudinaryField(max_length=255, verbose_name='video')),
                ('skill_c_description', models.CharField(max_length=250)),
                ('skill_x_name', models.CharField(max_length=50)),
                ('skill_x_icon', cloudinary.models.CloudinaryField(max_length=255, verbose_name='icon')),
                ('skill_x_video', cloudinary.models.CloudinaryField(max_length=255, verbose_name='video')),
                ('skill_x_description', models.CharField(max_length=250)),
            ],
            options={
                'verbose_name': 'agent',
                'verbose_name_plural': 'agents',
            },
        ),
    ]