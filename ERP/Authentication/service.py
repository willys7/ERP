from models import User, Rol
from rest_framework.authtoken.models import Token
from  UserModel import *

def AddUser(user):
    userModel = UserModel()
    for key, value in user.items():
        if(key == 'user_name'):
           userModel.user_name = value
        if(key == 'password'):
           userModel.password = value
        if(key =='rol'):
            userModel.rol = value
        if(key == 'name'):
            userModel.name = value
        

    print(userModel.name)

