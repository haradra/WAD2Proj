# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-03-07 16:45
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Messages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('messages', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Pet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('description', models.CharField(max_length=200)),
                ('species', models.CharField(max_length=30)),
                ('petPicture', models.ImageField(blank=True, upload_to='pet_images')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.CharField(max_length=30)),
                ('madeBy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('toWho', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pawpal.Pet')),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=128)),
                ('dateOfBirth', models.DateField()),
                ('profilePicture', models.ImageField(blank=True, upload_to='profile_images')),
                ('experience', models.IntegerField()),
                ('description', models.CharField(max_length=200)),
                ('showPets', models.BooleanField()),
                ('website', models.URLField(blank=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='messages',
            name='petId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pawpal.Pet'),
        ),
        migrations.AddField(
            model_name='messages',
            name='seekerUsername',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]