import uuid
class IngredientModel:
    
    def __init__(self):
        self.ingredient_guid = str(uuid.uuid4())
        self.name = ""
        self._type = ""
        self.cost = ""
        self.expiration_date = ""
        