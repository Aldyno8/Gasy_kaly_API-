from django.contrib import admin
from .models import *

# Register your models here.
class PlatsAdmin(admin.ModelAdmin):
    model = Plats
    list_display = ['name','category', 'date']
    
class IngredientAdmin(admin.ModelAdmin):
    model = Ingrédients
    list_display = ['name','quantity']
    
class UtilsAdmin(admin.ModelAdmin):
    model = Utils
    list_display = ['name']

class PrepaAdmin(admin.ModelAdmin):
    model = Preparation
    list_display = ['step','description']
    
class RateAdmin(admin.ModelAdmin):
    model = Rating
    list_display = ['rate', ]
    
class CommsAdmin(admin.ModelAdmin):
    model = Commentaire
    list_display = ['commentaire', ]
    
    
admin.site.register(Plats, PlatsAdmin)
admin.site.register(Ingrédients, IngredientAdmin)
admin.site.register(Preparation, PrepaAdmin)
admin.site.register(Utils, UtilsAdmin)
admin.site.register(Rating, RateAdmin)
admin.site.register(Commentaire, CommsAdmin)
