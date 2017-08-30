import datetime
class ProviderModel:
    name = ""
    nit = ""
    address = ""
    phone = ""
    email = ""

    def __init__(self, provider_data):
        for key, value in provider_data.items():
            if key == "name":
                self.name = value
            if key == "nit":
                self.nit = value
            if key == "address":
                self.address = value
            if key == "phone":
                self.phone = value
            if key == "email":
                self.email = value

    def ValidateProvider(self, provider):
        if provider.name == None or provider.name == "":
            raise Exception('Name is invalid')
        if provider.address == None or provider.address == "":
            raise Exception('Address is invalid')
        if provider.email == None or provider.email == "":
            raise Exception('Email is invalid')
        if provider.phone == None or provider.phone == "":
            raise Exception('Phone is invalid')
        if provider.nit == None or provider.nit == "":
            raise Exception('Nit is invalid')
        return True