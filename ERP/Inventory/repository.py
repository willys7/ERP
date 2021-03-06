from models import Store, Ingredient, Inventory
from Purchases.models import Purchase
from Authentication.models import Token
import datetime
from django.db import connection
from django.db.models import Count
from django.db import IntegrityError
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

def CreateNewStore(store):
    try:
        store_model = Store.objects.create_new_store(store)
        return store_model
    except IntegrityError as e:
        err = e.message.encode('utf-8')
        raise Exception(err)

def CreateNewIngredient(ingredient):
    try:
        ingredient_model = Ingredient.objects.create_new_ingredient(ingredient)
        return ingredient_model
    except IntegrityError as e:
        err = e.message.encode('utf-8')
        raise Exception(err)

def FindIfExistAuthToken(token_value):
    try:
        token = Token.objects.find_token_by_value(token_value)
        return token
    except:
        raise Exception("Invalid token")

def FindStoreByGuid(guid):
    try:
        store_model = Store.objects.find_store_by_guid(guid)
        return store_model
    except IntegrityError as e:
        err = e.message.encode('utf-8')
        raise Exception(err)
    
def FindIngredientByGuid(guid):
    try:
        ingredient_model = Ingredient.objects.find_ingredient_by_guid(guid)
        return ingredient_model
    except IntegrityError as e:
        err = e.message.encode('utf-8')
        raise Exception(err)

def FindPurchaseById(id):
    try:
       purchase_model = Purchase.objects.find_purchase_by_id(id)
       return purchase_model
    except IntegrityError as e:
        err = e.message.encode('utf-8')
        raise Exception(err)

def CreateNewPurchaseTransaction(transaction, store, ingredient, purchase):
    try:
        if purchase == "":
            transaction_model = Inventory.objects.create_new_transaction(transaction, store,
            ingredient)
            return transaction_model
        else:
            transaction_model = Inventory.objects.create_new_transaction_with_purchase(transaction, 
            store, ingredient, purchase)
            return transaction_model
    except IntegrityError as e:
        err = e.message.encode('utf-8')
        raise Exception(err)

def CreateNewSaleTransaction(transaction, store, ingredient):
    try:  
        transaction_model = Inventory.objects.create_new_transaction(transaction, store,
        ingredient)
        return transaction_model   
    except IntegrityError as e:
        err = e.message.encode('utf-8')
        raise Exception(err)


def ConsolidateInventoryByIngredientInStore(ingredient_name, store_guid):
    try:
        ingredient_existence = Inventory.objects.consolidate_inventory_by_ingredient_in_store(ingredient_name, store_guid)
        for key, value in ingredient_existence.items():
            return value
    except IntegrityError as e:
        err = e.message.encode('utf-8')
        raise Exception(err)