# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase, Client
from django.core.urlresolvers import reverse
from django.test.utils import setup_test_environment
from rest_framework.test import APIRequestFactory
from rest_framework.test import APIClient
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.utils.six import BytesIO
import json
import uuid
from time import time

from models import *
from Authentication import models
from Inventory import models
from service import *

# Create your tests here.

class PointOfSaleTest(TestCase):
    
    def setUp(self):
        self.api_client = APIClient()
        #create user
        self.api_client.post('/api-auth/user/', {"name":"William","user_name":"wil","password":"qwerty123","email":"da@gg.com","rol":"admin"}, format='json')
        self.limitstress = 0.5
        #get access token
        response = self.api_client.post('/api-auth/login/', {"user_name":"wil","password":"qwerty123"}, format='json')

        data = response.data
        json_data = json.loads(data)
        data = dict([(k.encode('ascii','ignore'), v.encode('ascii','ignore')) for k, v in json_data.items()])
        self.token = data["token"]

        #create store
        self.response_store = self.api_client.post('/api-inventory/store/',{"name":"Tienda Naranjo Mall","address":"zona 4","phone": 98989898,"email":"wo@g.com","token": self.token}, format='json')
        #create default ingredient
        self.response_ingredient = self.api_client.post('/api-inventory/ingredient/',{"name":"Zanahoria","_type":"Verdura","cost": 0.42,"token":self.token}, format='json')
        #create new product
        self.response_product = self.api_client.post('/api-pointofsale/product/',{"name":"IGO Asia","price":15,"token":self.token}, format='json')

        #add ingredient to the inventory
        data_ingredient = dict([(k.encode('ascii','ignore'), v.encode('ascii','ignore')) for k, v in self.response_ingredient.data.items()])
        data_store = dict([(k.encode('ascii','ignore'), v.encode('ascii','ignore')) for k, v in self.response_store.data.items()])
        model_trans = {
            "quantity" : 15,
	        "store_guid" : data_store["guid"],
	        "ingredient_guid" : data_ingredient["guid"],
	        "token" : self.token
        }
        response = self.api_client.post('/api-inventory/transaction/', model_trans, format='json')

    #Unit test
    def test_create_product_success(self):
        model = {
            "name":"IGO Buffalo",
            "price":15,
            "token": self.token
        }

        product, value = CreateNewProduct(model)
        self.assertEquals(product["name"], "IGO Buffalo")
        self.assertTrue(value)

    def test_create_product_fail(self):
        model = {
            "name":"IGO Asia",
            "price":15,
            "token": self.token
        }
        try:
            product = CreateNewProduct(model)
            self.assertTrue(False)
        except Exception, e:
            self.assertTrue(True)

    #Integration test
    def test_create_ricipe_sucess(self):
        data_ingredient = dict([(k.encode('ascii','ignore'), v.encode('ascii','ignore')) for k, v in self.response_ingredient.data.items()])
        data_store = dict([(k.encode('ascii','ignore'), v.encode('ascii','ignore')) for k, v in self.response_store.data.items()])
        data_product = dict([(k.encode('ascii','ignore'), v.encode('ascii','ignore')) for k, v in self.response_product.data.items()]) 
        
        model = {
            "product_guid": data_product["product_guid"],
            "ingredient_guid": data_ingredient["guid"],
            "quantity":1,
            "token": self.token
        }

        model_recipe, value = CreateNewRecipe(model)

        self.assertEquals("Zanahoria", model_recipe.ingredient.name)
        self.assertTrue(value)

    def test_create_recipe_fail(self):
        data_ingredient = dict([(k.encode('ascii','ignore'), v.encode('ascii','ignore')) for k, v in self.response_ingredient.data.items()])
        data_store = dict([(k.encode('ascii','ignore'), v.encode('ascii','ignore')) for k, v in self.response_store.data.items()])
        data_product = dict([(k.encode('ascii','ignore'), v.encode('ascii','ignore')) for k, v in self.response_product.data.items()]) 
        
        model = {
            "product_guid": "",
            "ingredient_guid": data_ingredient["guid"],
            "quantity":1,
            "token": self.token
        }

        try:
            model_recipe = CreateNewRecipe(model)
            self.assertTrue(False)

        except Exception, e:
            self.assertEquals("product_guid is invalid", str(e))
        
    