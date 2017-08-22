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

class User(models.Model):
    name = models.CharField(max_length=30)
    user_name = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=50)
    email = models.EmailField(verbose_name='email address', max_length=254, unique=True)
    objects = UserManager()
    def __str__(self):
        return self.user_name

class RolManager(models.Manager):
    def create_rol_for_user(self, user, rol):
        rol_model = self.create(user=user, rol=rol)
        return rol_model

class Rol(models.Model):
    rol = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    objects = RolManager()

class AuthTokenManager(models.Manager):
    def create_token_for_user(self, user):
        token = uuid.uuid4().hex
        last_activation = datetime.datetime.now()
        token_model = self.create(token=token,last_activation=last_activation,
        user=user)

class Token(models.Model):
    token = models.CharField(max_length=254, unique=True)
    date_created = models.DateField(auto_now=True)
    last_activation = models.DateTimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    objects = AuthTokenManager()
    