from models import Purchase, Provider
from Authentication.models import Token
from Inventory.models import Inventory
import datetime
from django.db import connection
from django.db.models import Count
from django.db import IntegrityError
import sys
reload(sys)
sys.setdefaultencoding("utf-8")


def FindIfExistAuthToken(token_value):
    try:
        token = Token.objects.find_token_by_value(token_value)
        return token
    except:
        raise Exception("Invalid token")

def CreateProvider(provider_model):
    try:
        provider = Provider.objects.create_new_provider(provider_model)
        return provider
    except IntegrityError as e:
        err = e.message.encode('utf-8')
        raise Exception(err)

def FindProviderByNit(nit):
    try:
        provider = Provider.objects.find_provider_by_nit(nit)
        return provider
    except IntegrityError as e:
        err = e.message.encode('utf-8')
        raise Exception(err)

def CreatePurchase(purchase, provider):
    try:
        purchase_model = Purchase.objects.create_new_purchase(purchase, provider)
        return purchase_model
    except IntegrityError as e:
        err = e.message.encode('utf-8')
        raise Exception(err)