from models import Store, Ingredient, Inventory
from Purchases.models import Purchase
from Authentication.models import Token
from rest_framework.authtoken.models import Token
from StoreModel import *
from IngredientModel import *
from repository import  *
from TransactionModel import *
import datetime
import dateutil.parser


def AddNewStore(store):
    if store == {}:
        raise Exception("Invalid store")
    storeModel = StoreModel(store)
    token = ""
    for key, value in store.items():
        if key == 'token':
            token = value

    if ValidateAuthToken(token):
        if storeModel.ValidateStore(storeModel):
            store_model = CreateNewStore(storeModel)
            return store_model
        else:
            raise Exception ("Invalid Store Model")
    else:
        raise Exception ("Invalid Token")

def AddNewIngredient(ingredient):
    if ingredient == {}:
        raise Exception("Invalid ingredient data")
    ingredientModel = IngredientModel(ingredient)
    token = ""
    for key, value in ingredient.items():
        if key == 'token':
            token = value 

    try:
        if ValidateAuthToken(token):
            if ingredientModel.ValidateIngredient(ingredientModel):
                ingredient_model = CreateNewIngredient(ingredientModel)
                return ingredient_model

    except Exception, e:
        raise Exception(str(e))

def HandleInventoryTransaction(transaction):
    if transaction == {}:
        raise Exception("Invalid transaction data")
    transactionModel = TransactionModel(transaction)
    token = ""
    purchase = ""
    store_guid = ""
    ingredient_guid = ""
    for key, value in transaction.items():
        if key == "ingredient_guid":
            ingredient_guid = value
        if key == "store_guid":
            store_guid = value
        if key == "token":
            token = value
        if key == "purchase":
            purchase = value
    
    if ValidateAuthToken(token):
        try:
            store_model = FindStoreByGuid(store_guid)
            ingredient_model = FindIngredientByGuid(ingredient_guid)
            transactionModel.calculate_total_amout_transaction(ingredient_model.cost)
            purchase_model = ""
            
            if purchase != "":
                purchase_model = FindPurchaseById(purchase)

            if transactionModel.quantity < 0:
                if ValidateExcistenceByTransaction(transactionModel.quantity, ingredient_guid, store_guid):
                    transaction_model = CreateNewTransaction(transactionModel, store_model,
                        ingredient_model, purchase_model)
                    return transaction_model
                else:
                    raise Exception("There is not enough stock in inventory")
                    
            transaction_model = CreateNewTransaction(transactionModel, store_model, ingredient_model, purchase_model)
            return transaction_model
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

def ValidateStore(store):
    if store.name == None or store.name == "":
        raise Exception('Name is invalid')
    if store.address == None or store.address == "":
        raise Exception('Address is invalid')
    if store.email == None or store.email == "":
        raise Exception('Email is invalid')
    if store.phone == None or store.phone == "":
        raise Exception('Phone is invalid')
    return True

def ValidateIngredient(ingredient):
    if ingredient.name == None or ingredient.name == "":
        raise Exception('Name is invalid')
    if ingredient._type == None or ingredient._type == "":
        raise Exception('Type is invalid')
    if ingredient.cost == None or ingredient.cost == 0:
        raise Exception('Cost is invalid')
    if ingredient.expiration_date != "":
        if ingredient.expiration_date < datetime.datetime.utcnow():
            raise Exception('Invalid date please check')

    return True

def ValidateExcistenceByTransaction(quantity, ingredient_guid, store_guid):
    try:
        existence_product = ConsolidateInventoryByIngredientInStore(ingredient_guid, store_guid)
        if existence_product < abs(quantity):
            return False
        else:
            return True
    except Exception, e:
        raise Exception(str(e))

def ConsolidateInventoryByProductInStore(ingredient_guid, store_guid):
    try:
        existence_product = ConsolidateInventoryByIngredientInStore(ingredient_guid, store_guid)
        return existence_product
    except Exception, e:
        raise Exception(str(e))

    


    
    
    
