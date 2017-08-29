# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.conf import settings
from Purchases.models import Purchase
import uuid
import datetime
from StoreModel import *
from django.db.models import Sum
# Create your models here.

#Store Model
class StoreManager(models.Manager):
    def create_new_store(self, store):
        try:
            store_model = self.create(store_guid=store.store_guid, name=store.name,
                address=store.address, phone=store.phone, email=store.email)
            return store_model
        except Exception, e:
            raise Exception("Invalid store data: " + str(e))

    def find_store_by_guid(self, guid):
        try:
            store_model = self.get(store_guid=guid)
            return store_model
        except Exception, e:
            raise Exception("Not found store by guid: " + str(e))

class Store(models.Model):
    store_guid = models.CharField(max_length=250, primary_key=True, unique=True)
    name = models.CharField(max_length=100, unique=True)
    address = models.CharField(max_length=100)
    phone = models.IntegerField()
    email = models.EmailField(verbose_name='email address', max_length=254, unique=True)
    objects = StoreManager()

#Ingredient Model
class IngredientManager(models.Manager):
    def create_new_ingredient(self, ingredient):
        try:
            if ingredient.expiration_date != "":
                ingredient_model = self.create(ingredient_guid=ingredient.ingredient_guid, 
                    name= ingredient.name, _type=ingredient._type, cost=ingredient.cost, 
                    expiration_date=ingredient.expiration_date)
            else:
                ingredient_model = self.create(ingredient_guid=ingredient.ingredient_guid, 
                    name= ingredient.name, _type=ingredient._type, cost=ingredient.cost)
            return ingredient_model
        except Exception, e:
            raise Exception("Invalid ingredet data: " + str(e))

    def find_ingredient_by_guid(self, guid):
        try:
            ingredient_model = self.get(ingredient_guid=guid)
            return ingredient_model
        except Exception, e:
            raise Exception("Not found ingredient by guid: " + str(e))  

class Ingredient(models.Model):
    ingredient_guid = models.CharField(max_length=250, primary_key=True, unique=True)
    name = models.CharField(max_length=100, unique=True)
    _type = models.CharField(max_length=100)
    cost = models.FloatField()
    expiration_date = models.DateField(blank=True, null=True)
    objects = IngredientManager()

#Inventory Model
class InventoryManager(models.Manager):
    def create_new_transaction(self, transaction, store, ingredient):
        try:
            transaction_model = self.create(store=store, ingredient=ingredient,
                quantity=transaction.quantity, cost=transaction.amount)
            return transaction_model
        except Exception, e:
            raise Exception("Invalid transaction data: " + str(e))

    def consolidate_inventory_by_ingredient_in_store(self, ingredient_guid, store_guid):
        try:
            existance = self.filter(store_id=store_guid, ingredient_id=ingredient_guid).aggregate(Sum('quantity'))
            return existance
        except Exception, e:
            raise Exception("Invalid transaction data: " + str(e))
     
class Inventory(models.Model):
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    cost = models.FloatField()
    date = models.DateField(auto_now=True)
    purchase = models.ForeignKey(Purchase, on_delete=models.CASCADE, blank=True, null=True)
    objects = InventoryManager()



    