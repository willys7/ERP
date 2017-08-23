class TokenResponseModel:
    
    def __init__(self, token, date_expiration, rol):
        self.token = token
        self.date_expiration = str(date_expiration)
        self.rol = rol