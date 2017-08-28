import uuid
class StoreModel:
    name = None
    address = ""
    phone = ""
    email = ""
    def __init__(self, store_data):
        self.store_guid = str(uuid.uuid4())
        for key, value in store_data.items():
            if key == 'name':
                self.name = value
            if key == 'address':
                self.address = value
            if key =='phone':
                self.phone = value
            if key == 'email':
                self.email = value
    
    def ValidateStore(self, store):
        if store.name == None or store.name == "":
            raise Exception('Name is invalid')
        if store.address == None or store.address == "":
            raise Exception('Address is invalid')
        if store.email == None or store.email == "":
            raise Exception('Email is invalid')
        if store.phone == None or store.phone == "":
            raise Exception('Phone is invalid')
        return True