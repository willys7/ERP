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

from models import *
from Authentication import models
from service import *
# Create your tests here.

class InventoryTest(TestCase):
    
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


    #Unit test

    def test_create_store_success(self):
        new_store = {
            "name":"Tienda Cayala",
            "address":"zona 16",
            "phone": 98989898,
            "email":"cayala@g.com",
            "token": self.token
        }
        model, value = AddNewStore(new_store)
        self.assertEquals(model["name"], "Tienda Cayala")
        self.assertTrue(value)

    def test_create_store_fail(self):
        
        new_store = {
            "name":"Tienda Naranjo Mall",
            "address":"zona 16",
            "phone": 98989898,
            "email":"cayala@g.com",
            "token": self.token
        }
        try:
            value = AddNewStore(new_store)
            self.assertTrue(False)
        
        except Exception, e:
            self.assertTrue(True)

    def test_create_ingredient_success(self):
        
        new_ingredient = {
            "name":"Tomate",
            "_type":"Verdura",
            "cost": 0.42,
            "token":self.token,
            "ingredient_guid": str(uuid.uuid4())
        }
        model, value = AddNewIngredient(new_ingredient)

        self.assertEquals(model["name"],"Tomate")
        self.assertTrue(True)

    
    def test_create_ingredient_fail(self):
        
        new_ingredient = {
            "name":"Zanahoria",
            "_type":"Verdura",
            "cost": 0.42,
            "token":self.token,
            "ingredient_guid": str(uuid.uuid4())
        }
        try:
            model = AddNewIngredient(new_ingredient)
            self.assertTrue(False)
        except Exception, e:
            self.assertTrue(True)
        
    #Integration test
    def test_create_transacction_successful(self):
        
        data_ingredient = dict([(k.encode('ascii','ignore'), v.encode('ascii','ignore')) for k, v in self.response_ingredient.data.items()])
        data_store = dict([(k.encode('ascii','ignore'), v.encode('ascii','ignore')) for k, v in self.response_store.data.items()])
        model_trans = {
            "quantity" : 5,
	        "store_guid" : data_store["guid"],
	        "ingredient_guid" : data_ingredient["guid"],
	        "token" : self.token
        }

        model, value = HandleInventoryTransaction(model_trans)
        self.assertTrue(value)

    def test_create_transacction_fail_is_not_enough_stock_in_inventory(self):
        data_ingredient = dict([(k.encode('ascii','ignore'), v.encode('ascii','ignore')) for k, v in self.response_ingredient.data.items()])
        data_store = dict([(k.encode('ascii','ignore'), v.encode('ascii','ignore')) for k, v in self.response_store.data.items()])
        model_trans = {
            "quantity" : -5,
	        "store_guid" : data_store["guid"],
	        "ingredient_guid" : data_ingredient["guid"],
	        "token" : self.token
        }
        try:
            model, value = HandleInventoryTransaction(model_trans)
            self.assertTrue(False)
        except Exception, e:
            self.assertEquals("There is not enough stock in inventory", str(e))

    
    

