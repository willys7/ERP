from models import Product, Invoice, Recipe, Buyer
from Purchases.models import Purchase
from Authentication.models import Token
from rest_framework.authtoken.models import Token
from ProductModel import *
from InvoiceModel import *
from repository import  *
from RecipeModel import *
from BuyerModel import *
import datetime
import dateutil.parser
import uuid


def CreateNewProduct(product):
    if product == {}:
        raise Exception("Invalid product data")
    productModel = ProductModel(product)
    print productModel.product_guid
    token = ""
    for key, value in product.items():
        if key == 'token':
            token = value 

    try:
        if ValidateAuthToken(token):
            if productModel.ValidateProduct(productModel):
                product_model = CreateProduct(productModel)
                return product_model

    except Exception, e:
        raise Exception(str(e))


def ValidateAuthToken(token_value): 
    try:
        token = FindIfExistAuthToken(token_value)
        date_active = token.last_activation + datetime.timedelta(hours=2)
        token_date = dateutil.parser.parse(str(date_active)).replace(tzinfo=None)
        now = datetime.datetime.utcnow()
        if token_date < now:
            return False
        else:
            return True
    except Exception, e:
        raise Exception(str(e))