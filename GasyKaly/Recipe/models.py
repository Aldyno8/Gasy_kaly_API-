from django.db import models
from django.contrib.auth.models import User
categories = {"Plats":"Plats", "Dessert":"Dessert", "Boisson":"Boisson"}

# Create your models here.
# Table qui va gérer les outils de préparation
class Utils(models.Model):
    name = models.CharField(max_length=50)
      
#  Table qui va gérer les Plats 
class Plats(models.Model):
    name = models.CharField(max_length=200)
    category = models.CharField(max_length=20, choices=categories)
    rate = models.FloatField(default=0)
    utils = models.ManyToManyField(Utils, related_name="utils")
    date = models.DateTimeField(auto_now_add=True, null=True)
    
    def __str__(self):
        return self.name
    
# Table qui va gérer les ingrédients
class Ingrédients(models.Model):
    name = models.CharField(max_length=50)
    quantity = models.CharField(max_length=10)
    plat = models.ForeignKey(Plats, on_delete=models.CASCADE, related_name="ingredient", null=True)
    
    def __str__(self):
        return self.name
    
# Table qui  renseigner sur la  préparation
class Preparation(models.Model):
    step = models.IntegerField()
    description = models.TextField()
    plat = models.ForeignKey(Plats, on_delete=models.CASCADE, related_name="preparation", null=True)
    
    def __str__(self):
        return self.description
     
# Table qui gère les notes
class Rating(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='rating', null=True)
    rate = models.FloatField()
    plat = models.ForeignKey(Plats, related_name='note', on_delete=models.CASCADE)
    
class Commentaire(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='commentaire')
    commentaire = models.TextField()
    plat = models.ForeignKey(Plats, related_name='commentaire', on_delete=models.CASCADE)
    

    