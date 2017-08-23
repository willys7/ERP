from models import User, Token, Rol
import datetime

def AddUserModel(user):
    try:
        user_model = User.objects.create_user(user)
        token_model = Token.objects.create_token_for_user(user_model)
        rol_model = Rol.objects.create_rol_for_user(user_model, user.rol)
        return rol_model, token_model
    except:
        raise Exception("Invalid user data, the user name already exist") 

def FindUserByUserName(user_name):
    try:
        user = User.objects.find_user_by_user_name(user_name)
        return user
    except:
        raise Exception("Invalid user name")

def FindAuthTokenByUserId(user_id):
    try:
        token = Token.objects.find_token_by_user_id(user_id)
        return token
    except:
        raise Exception("Problems with the Token")

def FindRolByUserId(user_id):
    try:
        rol = Rol.objects.find_rol_by_user_id(user_id)
        return rol
    except:
        raise Exception("User does not have rol")

def UpdateLastActivationToken(token_id):
    try:
        token = Token.objects.update_last_activate_token(token_id)
        return token
    except:
        raise Exception("Token does not exist")