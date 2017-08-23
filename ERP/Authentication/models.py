# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.conf import settings
from UserModel import *
import uuid
import datetime

# Create your models here.
class UserManager(models.Manager):
    def create_user(self, user):
        user_model = self.create(name=user.name, user_name=user.user_name,
        password=user.password, email=user.email)
        return user_model

    def find_user_by_user_name(self, user_name):
        user = self.get(user_name=user_name)
        return user

    def find_user_by_user_id(self, user_id):
        user = self.get(id=user_id)
        return user

class User(models.Model):
    name = models.CharField(max_length=30)
    user_name = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=50)
    email = models.EmailField(verbose_name='email address', max_length=254, unique=True)
    objects = UserManager()
    def __str__(self):
        return self.user_name


#ROL Model
class RolManager(models.Manager):
    def create_rol_for_user(self, user, rol):
        rol_model = self.create(user=user, rol=rol)
        return rol_model
    
    def find_rol_by_user_id(self, user_id):
        rol = self.get(user_id=user_id)
        return rol

class Rol(models.Model):
    rol = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    objects = RolManager()


#Auth Token Model
class AuthTokenManager(models.Manager):
    def create_token_for_user(self, user):
        token = uuid.uuid4().hex
        last_activation = datetime.datetime.utcnow()
        token_model = self.create(token=token,last_activation=last_activation,
        user=user)
        return token_model

    def find_token_by_user_id(self, user_id):
        token = self.get(user_id = user_id)
        return token
    
    def update_last_activate_token(self, token_id):
        token = self.get(id=token_id)
        token.last_activation = datetime.datetime.utcnow()
        token.save()
        return token


class Token(models.Model):
    token = models.CharField(max_length=254, unique=True)
    date_created = models.DateField(auto_now=True)
    last_activation = models.DateTimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    objects = AuthTokenManager()
    