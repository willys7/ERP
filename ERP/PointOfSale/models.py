# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from Inventory.models import Ingredient, Store
from django.db import models
from ProductModel import *
import uuid
import datetime
# Create your models here.

#Buyer Model
class BuyerManager(models.Manager):
    def create_new_buyer(self, buyer):
        try:
            if buyer.address == "":
                buyer.address = None
            if buyer.phone == "":
                buyer.address = None
    
            buyer_model = self.create(name=buyer.name, nit=buyer.nit, address=buyer.address,
                phone=buyer.phone)
            return buyer_model
        except Exception, e:
            raise Exception("Invalid transaction data: " + str(e))

    def find_buyer_by_nit(self, nit):
        try:
            buyer = self.get(nit=nit)
            return buyer
        except Exception, e:
            raise Exception("Invalid transaction data: " + str(e))

class Buyer(models.Model):
    name = models.CharField(max_length=100)
    nit = models.CharField(max_length=254, unique=True)
    address = models.CharField(max_length=254, blank=True, null=True)
    phone = models.IntegerField(blank=True, null=True)
    objects = BuyerManager()

#Invoice Model
class InvoiceManager(models.Manager):
    def create_new_invoice(self, invoice, buyer):
        try:
            invoice_model = self.create(buyer=buyer, amount=invoice.amount)
            return invoice_model
        except Exception, e:
            raise Exception("Invalid transaction data: " + str(e))

class Invoice(models.Model):
    buyer = models.ForeignKey(Buyer, on_delete=models.CASCADE)
    amount = models.FloatField()
    date = models.DateField(auto_now=True)
    objects = InvoiceManager()


#Product Model
class ProductManager(models.Manager):
    def create_new_product(self, product):
        try:
            product_model = self.create(product_guid=product.product_guid, name=product.name,
                price=product.price)
            return product_model
        except Exception, e:
            raise Exception("Invalid transaction data: " + str(e))

    def find_product_by_guid(self, guid):
        try:
            product = self.get(product_guid=guid)
            return product
        except Exception, e:
            raise Exception("Invalid transaction data: " + str(e))

class Product(models.Model):
    product_guid = models.CharField(max_length=250, primary_key=True, unique=True)
    name = models.CharField(max_length=250, unique= True)
    price = models.FloatField()
    objects = ProductManager()


#Recipe Model
class RecipeManager(models.Manager):
    def create_new_recipe(self, recipe, ingredeint, product):
        try:
            recipe_model = self.create(recipe_guid=recipe.ingredient_guid, product=product, 
                ingredient=ingredeint,
                quantity=recipe.quantity)
            return recipe_model
        except Exception, e:
            raise Exception("Invalid transaction data: " + str(e))
    
    def find_ingredient_by_product_by_product(self, products):
        try:
            ingredient_list = self.all().filter(product=products)
            return ingredient_list
        except Exception, e:
            raise Exception("Invalid transaction data: " + str(e))


class Recipe(models.Model):
    recipe_guid = models.CharField(max_length=250, primary_key=True, unique=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    objects = RecipeManager()



class ProductTransactionManager(models.Manager):
    def create_product_transaction(self, product, invoice, store, quantity):
        try:
            transaction_model = self.create(product=product, invoice=invoice, store=store,
                quantity=quantity)
            return transaction_model
        except Exception, e:
            raise Exception("Invalid transaction data: " + str(e))

    def find_all_transactions(self, start_date, end_date):
        try:
            transactions = []
            if start_date != "" and end_date != "":
                print "SI DATE"
                print start_date
                print end_date
                transactions_query = self.all().filter(date__lte=end_date).filter(date__gte=start_date)
            else:
                transactions_query = self.all()
            for transaction in transactions_query:
                transactions.append(transaction)
            return transactions
        except Exception, e:
            raise Exception("Invalid transaction data: " + str(e))

class ProductTransaction(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE)
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    date = models.DateField(auto_now=True)
    objects = ProductTransactionManager()