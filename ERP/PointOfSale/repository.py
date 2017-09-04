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
        print ingredient_model
        product_model = Product.objects.find_product_by_guid(recipe.product_guid)
        recipe_model = Recipe.objects.create_new_recipe(recipe, ingredient_model, product_model)
        return recipe_model
    except IntegrityError as e:
        err = e.message.encode('utf-8')
        raise Exception(err)