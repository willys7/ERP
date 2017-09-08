from models import Recipe, Product, Invoice, Buyer, ProductTransaction
from Inventory.models import Ingredient, Store
from Authentication.models import Token
import datetime
import urllib2
import json
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
        product_model = Product.objects.create_new_product(product)
        return product_model
    except IntegrityError as e:
        err = e.message.encode('utf-8')
        raise Exception(err)

def CreateBuyer(buyer):
    try:
        buyer_model = Buyer.objects.create_new_buyer(buyer)
        return buyer_model
    except IntegrityError as e:
        err = e.message.encode('utf-8')
        raise Exception(err)

def CreateRecipe(recipe):
    try:
        print recipe.product_guid
        ingredient_model = Ingredient.objects.find_ingredient_by_guid(recipe.ingredient_guid)
        print recipe.recipe_guid
        product_model = Product.objects.find_product_by_guid(recipe.product_guid)
        recipe_model = Recipe.objects.create_new_recipe(recipe, ingredient_model, product_model)
        return recipe_model
    except IntegrityError as e:
        err = e.message.encode('utf-8')
        raise Exception(err)

def FindBuyerByNit(nit):
    try:
        buyer_model = Buyer.objects.find_buyer_by_nit(nit)
        return buyer_model
    except IntegrityError as e:
        err = e.message.encode('utf-8')
        raise Exception(err)

def CreateInvoice(invoice, buyer):
    try:
        invoice_model = Invoice.objects.create_new_invoice(invoice, buyer)
        return invoice_model
    except IntegrityError as e:
        err = e.message.encode('utf-8')
        raise Exception(err)

def FindTransactions(start_date, end_date):
    try:
        transactions = {"transactions":[]}
        transactions_query = ProductTransaction.objects.find_all_transactions(start_date, end_date)
        print transactions_query
        for transaction in transactions_query:
            print transaction
            transaction_model = {
                "product":
                {
                    "product_name":transaction.product.name,
                    "product_price":transaction.product.price
                },
                "store":
                {
                    "store_name":transaction.store.name
                },
                "invoice":
                {
                    "amount": transaction.invoice.amount,
                    "invoice_identifier": transaction.invoice.id

                },
                "quantity": transaction.quantity,
                "date":transaction.date
            }
            print "BEFORE MODEL"
            print transaction_model
            transactions["transactions"].append(transaction_model)
            
        return transactions
    except IntegrityError as e:
        err = e.message.encode('utf-8')
        raise Exception(err)

def HandleTransactionOperations(invoice, transactions, token):
    try:
        products = []
        for product in transactions:
            store_guid = ""
            product_model = ""
            quantity = ""
            print "SIIIIIII"
            for key, value in product.items():
                if key == "store_guid":
                    store_model = Store.objects.find_store_by_guid(value)
                if key == "product_guid":
                    product_model = Product.objects.find_product_by_guid(value)
                    products.append(product_model)
                if key == "quantity":
                    quantity = value
            store_guid = store_model.store_guid
            transaction_model = ProductTransaction.objects.create_product_transaction(product_model,
                invoice, store_model, quantity)
        print "SIIIIIII"
        HandleInventoryTransactions(products, store_guid, token)
        return True
    except IntegrityError as e:
        err = e.message.encode('utf-8')
        raise Exception(err)

def HandleInventoryTransactions(products, store_guid, token):
    try:
        print "PRODUCTS"
        print products
        for product in products:
            ingredients = Recipe.objects.find_ingredient_by_product_by_product(product)
            for ingredient in ingredients:
                ingredient_model = {
                    "quantity": ingredient.quantity * (-1),
                    "store_guid": store_guid,
                    "ingredient_guid": ingredient.ingredient.ingredient_guid,
                    "token":token
                }
                print "YES MODEL INGREDIENT"
                print ingredient_model
                url = "http://localhost:8000/api-inventory/transaction/"
                opener = urllib2.build_opener(urllib2.HTTPHandler)
                request = urllib2.Request(url, data=json.dumps(ingredient_model))
                request.add_header("Content-Type", "application/json")
                response = opener.open(request)
                print response.read()

    except IntegrityError as e:
        err = e.message.encode('utf-8')
        raise Exception(err) 
