from rest_framework import serializers
from .models import *

class UtilsSerialisers(serializers.ModelSerializer):
    class Meta:
        model = Utils
        fields = '__all__'

class RecipeSerializers(serializers.ModelSerializer):
    class Meta:
        model = Plats
        fields = ['id', 'name', 'category', 'rate', 'date', 'utils', 'image']
    utils = UtilsSerialisers(many=True)
        
class Ingredientsserialisers(serializers.ModelSerializer):
    class Meta:
        model = Ingrédients
        fields = ['name', 'quantity']
        
class PrepaSerialiser(serializers.ModelSerializer):
    class Meta:
        model = Preparation
        fields = ['step', 'description']

class PrepaSerialisers(serializers.Serializer):
    plats = RecipeSerializers()
    ingredients = Ingredientsserialisers(many=True)
    preparation = PrepaSerialiser(many=True)