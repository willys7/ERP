# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-04 21:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Inventory', '0005_inventory_purchase'),
        ('PointOfSale', '0006_producttransaction_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='producttransaction',
            name='store',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Inventory.Store'),
            preserve_default=False,
        ),
    ]
