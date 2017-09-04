import uuid
import datetime
class ProductModel:
    product_guid = str(uuid.uuid4())
    name = ""
    price = ""

    def __init__(self, product):
        for key, value in product.items():
            if key == 'name':
                self.name = value
            if key == 'price':
                self.price = value
        

    def ValidateProduct(self, product):
        if product.name == None or product.name == "":
            raise Exception('Name is invalid')
        if product.price == None or product.price == "" or product.price < 1:
            raise Exception('Price is invalid')
        
        return True  