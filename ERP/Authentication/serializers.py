from models import User, Rol
from rest_framework import serializers

class UserSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=30)
    user_name = serializers.CharField(max_length=50, required=True)
    password = serializers.CharField(max_length=50, required=True)
    email = serializers.EmailField(max_length=254)
    rol = serializers.CharField(max_length=50)
    
