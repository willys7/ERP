from models import Store, Ingredient, Inventory
from Authentication.models import Token
import datetime
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
        print "Repository Token"
        token = Token.objects.find_token_by_value(token_value)
        print "Find token"
        return token
    except:
        raise Exception("Invalid token")