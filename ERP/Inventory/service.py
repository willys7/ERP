from models import Store, Ingredient, Inventory
from Authentication.models import Token
from rest_framework.authtoken.models import Token
from StoreModel import *
from IngredientModel import *
from repository import  *
import datetime
import dateutil.parser


def AddNewStore(store):
    if store == {}:
        raise Exception("Invalid store")
    storeModel = StoreModel(store)
    token = ""
    print store
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
        raise Exception("Invalid store")
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

def ValidateAuthToken(token_value): 
    try:
        token = FindIfExistAuthToken(token_value)
        print "Service Token"
        date_active = token.last_activation + datetime.timedelta(hours=2)
        token_date = dateutil.parser.parse(str(date_active)).replace(tzinfo=None)
        now = datetime.datetime.utcnow()
        if token_date < now:
            return False
        else:
            print "TRUE"
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

#def HandleInventoryTransaction(transaction):
    
