import uuid
import datetime
class RecipeModel:
    recipe_guid = str(uuid.uuid4())
    product_guid = ""
    ingredient_guid = ""
    quantity = ""
    

    def __init__(self, recipe):
        for key, value in recipe.items():
            if key == 'product_guid':
                self.product_guid = value
            if key == 'ingredient_guid':
                self.ingredient_guid = value
            if key == 'quantity':
                self.quantity = value
            

    def ValidateRecipe(self, recipe):
        if recipe.product_guid == None or recipe.product_guid == "":
            raise Exception('product_guid is invalid')
        if recipe.ingredient_guid == None or recipe.ingredient_guid == "":
            raise Exception('product_guid is invalid')
        if recipe.quantity == None or recipe.quantity == "" or recipe.quantity < 1:
            raise Exception('quantity is invalid')
        
        return True  