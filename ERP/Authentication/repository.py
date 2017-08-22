from models import User, Token, Rol

def AddUserModel(user):
    try:
        user_model = User.objects.create_user(user)
        token_model = Token.objects.create_token_for_user(user_model)
        rol_model = Rol.objects.create_rol_for_user(user_model, user.rol)
        return True
    except:
        raise Exception("Invalid user data, the user name already exist") 