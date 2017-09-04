import uuid
import datetime
class IngredientModel:
    nit = ""
    name = ""
    address = ""
    phone = ""

    def __init__(self, ingredient):
        for key, value in ingredient.items():
            if key == 'name':
                self.name = value
            if key == 'nit':
                self.nit = value
            if key =='address':
                self.address = value
            if key == 'phone':
                self.phone = value
        

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