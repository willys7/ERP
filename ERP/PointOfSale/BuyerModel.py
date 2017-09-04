import uuid
import datetime
class BuyerModel:
    nit = ""
    name = ""
    address = ""
    phone = ""

    def __init__(self, buyer):
        for key, value in buyer.items():
            if key == 'name':
                self.name = value
            if key == 'nit':
                self.nit = value
            if key =='address':
                self.address = value
            if key == 'phone':
                self.phone = value
        

    def ValidateBuyer(self, buyer):
        if buyer.name == None or buyer.name == "":
            raise Exception('Name is invalid')
        if buyer.nit == None or buyer.nit == "":
            raise Exception('nit is invalid')
        if buyer.address == None or buyer.address == "":
            raise Exception('address is invalid')
        if  buyer.phone == None or buyer.phone == "":
            raise Exception('Invalid Phone')

        return True  