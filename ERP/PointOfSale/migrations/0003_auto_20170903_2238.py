# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-04 04:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PointOfSale', '0002_product_recipe'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buyer',
            name='phone',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
