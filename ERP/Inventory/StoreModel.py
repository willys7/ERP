import uuid
class StoreModel:
    
    def __init__(self):
        self.store_guid = str(uuid.uuid4())
        self.name = ""
        self.address = ""
        self.phone = ""
        self.email = ""
        