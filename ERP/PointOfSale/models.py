# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

#Buyer Model
class Buyer(models.Model):
    name = models.CharField(max_length=100)
    nit = models.CharField(max_length=254, unique=True)
    address = models.CharField(max_length=254, blank=True, null=True)
    phone = models.IntegerField()


#Invoice Model
class Invoice(models.Model):
    buyer = models.ForeignKey(Buyer, on_delete=models.CASCADE)
    amount = models.FloatField()
    date = models.DateField(auto_now=True)
    #objects = PurchaseManager()
