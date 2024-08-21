from django.urls import path
from .views import *
urlpatterns = [
    path('', RecipeList.as_view(), name="Recipe"),
    path('preparation/<int:id>/', RecipeDetails.as_view(), name="Recette"),
    path('AddRecipe/', AddRecipe.as_view(), name='new recipe'),
    path('Rating/<int:id>/', RatingRecipe.as_view(), name='rate'),
    path('Comment/<int:id>/', CommentRecipe.as_view(), name='comment')
    
]
