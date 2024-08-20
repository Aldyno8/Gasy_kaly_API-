from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import *
from .serializers import *

# Create your views here.
# List des recettes existante dans la bdd
class RecipeList(APIView):
    def get(self, request, *args, **kwargs):
        try:
            recipe = Plats.objects.all()
            plat = RecipeSerializers(recipe, many=True)
            return Response(plat.data, status=status.HTTP_200_OK)
        
        except Exception as b:
            return Response({"message":str(b)})

# Détails pour chaque Recettes
class RecipeDetails(APIView):
    def get(self, request, id):
        plats = Plats.objects.get(id = id)
        try:
            ingredients = plats.ingredient.all()
            prepa = plats.preparation.all()

            
            recette = {
                "plats":plats,
                "ingredients":ingredients,
                "preparation":prepa
            }
            recipe = PrepaSerialisers(recette).data
            return Response(recipe, status=status.HTTP_200_OK)

        except Exception as b:
            return Response({"message":str(b)}, status=status.HTTP_400_BAD_REQUEST)
        
# Ajouter une nouvelle recettes
class AddRecipe(APIView):
    def post(self, request, *args, **kwargs):
        name = request.data.get('name')
        category = request.data.get('category')
        utils = request.data.get('utils')
        ingredients = request.data.get('ingredients')
        preparation = request.data.get('preparation')
        
        try:
            util_list = [] # liste qui va stocker les outils nécessaire
            for util in utils:
                create = Utils.objects.create(name=util) # sauvegarde des outils danns la bdd
                util_list.append(create)
            
            plat = Plats.objects.create(name=name, category=category) # sauvegarde du plats dans la base de données
            plat.utils.add(*util_list)
            
            if plat:       
                # Ajout des étapes de la préparation
                for  description in preparation:
                    step = Preparation.objects.create(description=description, step=preparation.index(description)+1, plat=plat)
                
                # Ajout des ingredient pour la recette    
                for ingredient, quantity in ingredients.items():
                    print(type(ingredients))
                    ingredient = Ingrédients.objects.create(name=ingredient, quantity= quantity, plat=plat)
                    
                    
                return Response({"message":"La recette a bien été ajouté"}, status=status.HTTP_201_CREATED)
            
            else:
                return Response({"message":"Informations invalide"}, status=status.HTTP_400_BAD_REQUEST)
            
        except Exception as b:
            return Response({"message":str(b)}, status=status.HTTP_400_BAD_REQUEST)

# Notation de plats
class RatingRecipe(APIView):
    def post(self, request, *args, **kwargs):
        id_plats = kwargs.get('id')
        rate = request.data.get('rate')
        
        try:
            plat = Plats.objects.get(id=id_plats)
            rating = Rating.objects.create(rate=rate, plat=plat)
            
            if not rating:
                return Response({"message":"erreur lors de la notation"}, status=status.HTTP_400_BAD_REQUEST)
            
            rate_list = plat.note.all()
            total = 0 
            for rate in rate_list:
                note = rate.rate
                total = total + note
                
            moyenne = total / len(rate_list)
            plat.rate = moyenne
            plat.save()
            
            
            return Response({"message":"note enregistrée"}, status=status.HTTP_201_CREATED)
        
        except Exception as b:
            return Response({"message": str(b)}, status=status.HTTP_400_BAD_REQUEST)
            
        
                
        