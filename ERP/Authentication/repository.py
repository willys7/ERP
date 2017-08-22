from models import *
from rest_framework.authtoken.models import Token

def AddUserModel(user):
    try:
        user_model = User.objects.create_user(user)
        return True
    except:
        raise Exception("Invalid user data, the user name already exist") 