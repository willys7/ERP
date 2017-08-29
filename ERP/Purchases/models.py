# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.conf import settings
import uuid
import datetime
from django.db.models import Sum
# Create your models here.

#Provider Model
class ProviderManager(models.Manager):
    def create_new_provider(self, provider):
        try:
            provider_model = self.create(name=provider.name, nit=provider.nit,
            address=provider.address, phone=provider.phone, email=provider.email)
            return provider_model
        except Exception, e:
            raise Exception("Invalid store data: " + str(e))

    def find_provider_by_nit(self, nit):
        try:
            provider_model = self.get(nit=nit)
            return provider_model
        except Exception, e:
            raise Exception("Not found store by guid: " + str(e))
    
    def find_provider_by_name(self, name):
        try:
            provider_model = self.get(name=name)
            return provider_model
        except Exception, e:
            raise Exception("Not found store by guid: " + str(e))

class Provider(models.Model):
    name = models.CharField(max_length=100)
    nit = models.CharField(max_length=100, unique=True)
    address = models.CharField(max_length=100)
    phone = models.IntegerField()
    email = models.EmailField(verbose_name='email address', max_length=254, unique=True)
    objects = ProviderManager()

#Purchase Model
class PurchaseManager(models.Manager):
    def create_new_provider(self, purchase, provider):
        try:
            purchase_model = self.create(provider=provider, amount=purchase.amount)
            return purchase_model
        except Exception, e:
            raise Exception("Invalid store data: " + str(e))


class Purchase(models.Model):
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE)
    amount = models.FloatField()
    date = models.DateField(auto_now=True)

