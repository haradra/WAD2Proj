# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-03-22 12:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pawpal', '0012_auto_20180322_1207'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pet',
            name='location',
            field=models.CharField(max_length=128),
        ),
        migrations.AlterField(
            model_name='pet',
            name='species',
            field=models.CharField(choices=[('DOG', 'Dog'), ('CAT', 'Cat'), ('LIZARD', 'Lizard'), ('REPTILE', 'Reptile'), ('BIRD', 'Bird'), ('HAMSTER', 'Hamster')], max_length=10),
        ),
    ]