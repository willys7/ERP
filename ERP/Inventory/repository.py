from models import Store, Ingredient, Inventory
from Authentication.models import Token
import datetime

def CreateNewStore(store):
    try:
        store_model = Store.objects.create_new_store(store)
        return store_model
    except:
        raise Exception("Invalid store data")

def FindIfExistAuthToken(token):
    try:
        token = Token.objects.find_token_by_value(token)
        return token
    except:
        raise Exception("Invalid store data")