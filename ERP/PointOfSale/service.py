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
    token = ""
    for key, value in product.items():
        if key == 'token':
            token = value 

    try:
        if ValidateAuthToken(token):
            if productModel.ValidateProduct(productModel):
                product_model = CreateProduct(productModel)
                model = {
                    "product_guid":product_model.product_guid,
                    "name": product_model.name
                }
                return model, True

    except Exception, e:
        raise Exception(str(e))

def CreateNewBuyer(buyer):
    if buyer == {}:
        raise Exception("Invalid buyer data")
    buyerModel = BuyerModel(buyer)
    token = ""
    for key, value in buyer.items():
        if key == 'token':
            token = value 

    try:
        if ValidateAuthToken(token):
            if buyerModel.ValidateBuyer(buyerModel):
                buyer_model = CreateBuyer(buyerModel)
                return buyer_model

    except Exception, e:
        raise Exception(str(e))

def CreateNewRecipe(recipe):
    if recipe == {}:
        raise Exception("Invalid recipe data")
    recipeModel = RecipeModel(recipe)
    token = ""
    for key, value in recipe.items():
        if key == 'token':
            token = value 

    try:
        if ValidateAuthToken(token):
            if recipeModel.ValidateRecipe(recipeModel):
                recipe_model = CreateRecipe(recipeModel)
                return recipe_model, True

    except Exception, e:
        raise Exception(str(e))

def FindAllTransactions(data):
    try:
        start_date = ""
        end_date = ""
        token = ""
        for key, value in data.items():
            if key == "start_date":
                start_date = dateutil.parser.parse(value)
            if key == "end_date":
                end_date = dateutil.parser.parse(value)
            if key == "token":
                token = value

        if ValidateAuthToken(token):      
            transactions = FindTransactions(start_date, end_date)
        return transactions
    except Exception, e:
        raise Exception(str(e))

def HandleInvoice(invoice):
    if invoice == {}:
        raise Exception("Invalid purchase")
    try:
        invoiceModel = InvoiceModel(invoice)
        token = ""
        buyer_nit = ""
        for key, value in invoice.items():
            if key == "token":
                token = value
            if key == "nit":
                buyer_nit = value
                
        print buyer_nit
        print token
        
        if ValidateAuthToken(token):
            if invoiceModel.ValidateInvoice(invoiceModel):
                buyer = FindBuyerByNit(buyer_nit)
                invoice = CreateInvoice(invoiceModel, buyer)
                transactions = HandleTransactionOperations(invoice, invoiceModel.products, token)
            if transactions:
                return invoice
            else:
                return "problem to handle a transaction"
    except Exception, e:
        raise Exception (str(e))

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