from models import Recipe, Product, Invoice, Buyer
from Inventory.models import Ingredient
from Authentication.models import Token
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

def CreateProduct(product):
    try:
        product = Product.objects.create_new_product(product)
        return product
    except IntegrityError as e:
        err = e.message.encode('utf-8')
        raise Exception(err)
