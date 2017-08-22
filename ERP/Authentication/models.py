# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from UserModel import *

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

class Rol(models.Model):
    rol = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)