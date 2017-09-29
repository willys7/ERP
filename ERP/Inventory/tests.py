# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase, Client
from django.core.urlresolvers import reverse
from django.test.utils import setup_test_environment

from models import *
from Authentication import models
# Create your tests here.

class InventoryTest(TestCase):
    
    def setUp(self):
        
