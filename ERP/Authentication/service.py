from models import User, Rol
from rest_framework.authtoken.models import Token
from  UserModel import *
from repository import AddUserModel, FindUserByUserName, FindAuthTokenByUserId, FindRolByUserId
from  TokenResponseModel import *
import datetime

def AddUser(user):
    print(user)
    if user == {}:
        raise Exception("Invalid User")
    
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

    if(validate):
        print(AddUserModel(userModel))


def ValidateUserCredentials(user_name, password):
    user = FindUserByUserName(user_name)
    if user == None:
        raise Exception ("Invalid user name")
    else:
        if(user.password == password):
            token = FindAuthTokenByUserId(user.id)
            rol = FindRolByUserId(user.id)
            date = token.last_activation + datetime.timedelta(hours=3)
            response_token = TokenResponseModel(token.token, date, rol.rol)
            print response_token
            return response_token
        else:
            raise Exception("Invalid password")

def ValidateUser(user):
    
    if user.name == None or user.name == "":
        raise Exception('Name is invalid')
    if user.user_name == None or user.user_name == "":
        raise Exception('User Name is invalid')
    if user.email == None or user.email == "":
        raise Exception('Email is invalid')
    if user.password == None or user.password == "":
        raise Exception('Password is invalid')
    if user.rol == None or user.rol == "":
        raise Exception('Rol is invalid')  
    return True
    
def ExtractCredentialsFromJson(credentials):
    print 'extract'
    print credentials
    user_name = ""
    password = ""
    for key, value in credentials.items():
        if key == "user_name":
            user_name = value
        if key == "password":
            password = value

    print(user_name, password)
    return user_name, password
