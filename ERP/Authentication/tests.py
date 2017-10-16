# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase, Client
from django.core.urlresolvers import reverse
from django.test.utils import setup_test_environment
from rest_framework.test import APIRequestFactory
from rest_framework.test import APIClient


from models import User, Token, Rol
from time import time
from  UserModel import *
from service import *
import graphitesend

class AuthTest(TestCase):

    def setUp(self):
        #setup_test_environment()
        self.user_model = UserModel()
        self.user_model.name = "william"
        self.user_model.email = "w@gmail.com"
        self.user_model.user_name = "wil"
        self.user_model.password = "qwerty123"
        self.success_tests = 0

        self.user = User.objects.create_user(self.user_model)
        self.user.save()
        self.client = Client()
        self.api_client = APIClient()
        self.api_client.post('/api-auth/user/', {"name":"alejandro","user_name":"daniel","password":"qwerty123","email":"da@gg.com","rol":"admin"}, format='json')
        self.limitstress = 0.5
        graphitesend.init(graphite_server='13.59.62.190')
    #Unit test
    def test_create_user_success(self):
        new_user = {
            "name":"daniel",
            "user_name":"daj",
            "password":"qwerty123",
            "email":"daj@gg.com",
            "rol":"admin"
        }

        token, value = AddUser(new_user)
        graphitesend.send('Successfull_test',2)
        self.assertTrue(value)

    def test_create_user_with_same_username_faild(self):
        new_user = {
            "name":"william",
            "user_name":"wil",
            "password":"qwerty123",
            "email":"w@gmail.com",
            "rol":"admin"
        }
        var = AddUser(new_user)
        graphitesend.send('Successfull_test',2)
        self.assertEqual("Invalid user name", var)

    def test_create_user_without_password_faild(self):
        new_user = {
            "name":"william",
            "user_name":"wil",
            "password":"",
            "email":"w@gmail.com",
            "rol":"admin"
        }
        var = AddUser(new_user)
        graphitesend.send('Successfull_test',2)
        self.assertEqual("Invalid password", var)

    def test_get_token_success(self):
        new_user = {
            "name":"test",
            "user_name":"test",
            "password":"qwerty123",
            "email":"testj@gg.com",
            "rol":"admin"
        }

        token, value = AddUser(new_user)
        value = ValidateUserCredentials("test","qwerty123")
        graphitesend.send('Successfull_test',2)
        self.assertTrue(value)

    def test_get_token_faild(self):
        new_user = {
            "name":"test",
            "user_name":"test",
            "password":"qwerty123",
            "email":"testj@gg.com",
            "rol":"admin"
        }

        token, value = AddUser(new_user)
        value = ValidateUserCredentials("test","qwerty")
        graphitesend.send('Successfull_test',2)
        self.assertEqual("Invalid user name or password", value)
        self.assertTrue(value)


    
    #Stress tests
    def test_stress_create_user(self):
        start_time = time()
        self.api_client.post('/api-auth/user/', {"name":"alejandro","user_name":"daniel","password":"qwerty123","email":"da@gg.com","rol":"admin"}, format='json')
        elapsed_time = time() - start_time
        value = False
        if(self.limitstress > elapsed_time  ):
            value = True
            graphitesend.send('Successfull_test',2)
        else:
            graphitesend.send('Successfull_test',1)
        
        
        graphitesend.send('Response_time',elapsed_time)
        self.assertTrue(value)

    def test_stress_get_token(self):
        start_time = time()
        response = self.api_client.post('/api-auth/login/', {"user_name":"daniel","password":"qwerty123"}, format='json')
        elapsed_time = time() - start_time
        value = False
        if(self.limitstress > elapsed_time):
            value = True
            graphitesend.send('Successfull_test',2)
        else:
            value = False
            graphitesend.send('Successfull_test',1)
        
        
        graphitesend.send('Response_time',elapsed_time)
        self.assertTrue(value)