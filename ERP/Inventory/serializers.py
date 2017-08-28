from models import Store, Ingredient, Inventory
from rest_framework import serializers

class StoreSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    address = serializers.CharField(max_length=100)
    phone = serializers.IntegerField()
    email = serializers.EmailField(max_length=254)
    token = serializers.CharField()

class IngredientSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    _type = serializers.CharField(max_length=100)
    cost = serializers.FloatField()
    expiration_date = serializers.DateField()
    token = serializers.CharField()