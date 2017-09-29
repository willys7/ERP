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

from models import *
from Authentication import models
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

