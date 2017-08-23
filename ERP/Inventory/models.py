# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.conf import settings
import uuid
import datetime

# Create your models here.

#Store Model
class Store(models.Model):
    store_guid = models.CharField(max_length=250, primary_key=True, unique=True)
    name = models.CharField(max_length=100, unique=True)
    address = models.CharField(max_length=100)
    phone = models.IntegerField()
    email = models.EmailField(verbose_name='email address', max_length=254, unique=True)


#Ingredient Model
class Ingredient(models.Model):
    ingredient_guid = models.CharField(max_length=250, primary_key=True, unique=True)
    name = models.CharField(max_length=100, unique=True)
    _type = models.CharField(max_length=100)
    expiration_date = models.DateField(blank=True, null=True)


#Inventory Model
class Inventory(models.Model):
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    