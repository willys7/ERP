# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=30)
    user_name = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=50)
    email = models.EmailField(verbose_name='email address', max_length=254, unique=True)
    def __str__(self):
        return self.user_name

class Rol(models.Model):
    rol = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)