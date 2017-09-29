from models import User, Rol
from rest_framework.authtoken.models import Token
from  UserModel import *
from repository import AddUserModel, FindUserByUserName, FindAuthTokenByUserId, FindRolByUserId, UpdateLastActivationToken
from  TokenResponseModel import *
import datetime

def AddUser(user):
    if user == {}:
        return "Invalid User Model"
    
    userModel = UserModel()
    
    for key, value in user.items():
        if key == 'user_name':
            userModel.user_name = value
        if key == 'password':
            userModel.password = value
        if key =='rol':
            userModel.rol = value
        if key == 'name':
            userModel.name = value
        if key == 'email':
            userModel.email = value
    
    validate = ValidateUser(userModel)

    if validate == "true":
        try:
            rol, token = AddUserModel(userModel)
            date = token.last_activation + datetime.timedelta(hours=2)
            return TokenResponseModel(token.token, date, rol.rol),True
        except:
            return "Invalid user name"
    else:
        return validate


def ValidateUserCredentials(user_name, password):
    user = FindUserByUserName(user_name)
    if user == None:
        return ("Invalid user name")
    else:
        if(user.password == password):
            token = FindAuthTokenByUserId(user.id)
            new_token = UpdateLastActivationToken(token.id)
            rol = FindRolByUserId(user.id)
            date = new_token.last_activation + datetime.timedelta(hours=2)
            response_token = TokenResponseModel(new_token.token, date, rol.rol)
            return response_token, True
        else:
            return ("Invalid user name or password")

def ValidateUser(user):
    
    if user.name == None or user.name == "":
        return ('Name is invalid')
    if user.user_name == None or user.user_name == "":
        return ('User Name is invalid')
    if user.email == None or user.email == "":
        return ('Email is invalid')
    if user.password == None or user.password == "":
        return ('Invalid password')
    if user.rol == None or user.rol == "":
        return ('Rol is invalid')  
    return "true"
    
def ExtractCredentialsFromJson(credentials):
    user_name = ""
    password = ""
    for key, value in credentials.items():
        if key == "user_name":
            user_name = value
        if key == "password":
            password = value

    return user_name, password
