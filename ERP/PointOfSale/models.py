# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from Inventory.models import Ingredient
from django.db import models

# Create your models here.

#Buyer Model
class Buyer(models.Model):
    name = models.CharField(max_length=100)
    nit = models.CharField(max_length=254, unique=True)
    address = models.CharField(max_length=254, blank=True, null=True)
    phone = models.IntegerField()
    #objects = PurchaseManager()

#Invoice Model
class Invoice(models.Model):
    buyer = models.ForeignKey(Buyer, on_delete=models.CASCADE)
    amount = models.FloatField()
    date = models.DateField(auto_now=True)
    #objects = PurchaseManager()

class Product(models.Model):
    product_guid = models.CharField(max_length=250, primary_key=True, unique=True)
    name = models.CharField(max_length=250, unique= True)
    price = models.FloatField()

class Recipe(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.IntegerField()