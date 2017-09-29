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

class AuthTest(TestCase):

    def setUp(self):
        #setup_test_environment()
        self.user_model = UserModel()
        self.user_model.name = "william"
        self.user_model.email = "w@gmail.com"
        self.user_model.user_name = "wil"
        self.user_model.password = "qwerty123"

        self.user = User.objects.create_user(self.user_model)
        self.client = Client()
        self.api_client = APIClient()
        self.limitstress = 0.5

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
        self.assertEqual("Invalid user name or password", value)
        self.assertTrue(value)


    
