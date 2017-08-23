# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.conf import settings
import uuid
import datetime
from StoreModel import *
# Create your models here.

#Store Model
class StoreManager(models.Manager):
    def create_new_store(self, store):
        store_model = self.create(store_guid=store.store_guid, name=store.name,
            address=store.address, phone=store.phone, email=store.email)
        return store_model

class Store(models.Model):
    store_guid = models.CharField(max_length=250, primary_key=True, unique=True)
    name = models.CharField(max_length=100, unique=True)
    address = models.CharField(max_length=100)
    phone = models.IntegerField()
    email = models.EmailField(verbose_name='email address', max_length=254, unique=True)
    objects = StoreManager()

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

    