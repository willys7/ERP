from models import Store, Ingredient, Inventory
from Authentication.models import Token
from rest_framework.authtoken.models import Token
from StoreModel import *
from repository import  *
import datetime


def AddNewStore(store):
    if store == {}:
        raise Exception("Invalid store")
    storeModel = StoreModel()

    for key, value in store.items():
        if key == 'name':
            storeModel.name = value
        if key == 'address':
            storeModel.address = value
        if key =='phone':
            storeModel.phone = value
        if key == 'email':
            storeModel.email = value
    if ValidateStore(storeModel):
        store_model = CreateNewStore(storeModel)
        return store_model
    else:
        raise Exception ("Invalid Store Model")


def ValidateAuthToken(token):
    
    try:
        token = FindIfExistAuthToken(token)
        date_active = token.last_activation + datetime.timedelta(hours=2)
        if date_active < datetime.datetime.utcnow():
            return False
        else:
            return True
    except:
        raise Exception("Invalid Auth Token")

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