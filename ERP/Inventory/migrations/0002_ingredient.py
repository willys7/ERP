# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-23 05:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Inventory', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('ingredient_guid', models.CharField(max_length=250, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=100, unique=True)),
                ('_type', models.CharField(max_length=100)),
                ('expiration_date', models.DateField(blank=True, null=True)),
            ],
        ),
    ]
