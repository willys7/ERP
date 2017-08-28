import uuid
import datetime
class IngredientModel:
    ingredient_guid = str(uuid.uuid4())
    name = ""
    _type = ""
    cost = ""
    expiration_date = ""

    def __init__(self, ingredient):
        for key, value in ingredient.items():
            if key == 'name':
                self.name = value
            if key == '_type':
                self._type = value
            if key =='cost':
                self.cost = value
            if key == 'expiration_date':
                self.expiration_date = value
        

    def ValidateIngredient(self, ingredient):
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