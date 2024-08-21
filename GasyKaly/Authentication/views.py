from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.models import User
from rest_framework import status

from .serializers import *

# Create your views here.
# Création de nouveau compte
class UserResigter(APIView):
    # {"username":"aldynot", "email":"aldynobruel@gmail.com", "password":"fake"}
    def post(self, request):
        username = request.data.get('username')
        email = request.data.get('email')
        password = request.data.get('password')
        try:
            created, user = User.objects.get_or_create(
                username=username,
                email=email, 
                password=password
            )
            if created:
                return Response({"message":"User create successfully!"},
                status=status.HTTP_201_CREATED )
            else:
                return Response({"message":"Un utilisateur avec les meme identifiants existe déja"},
                                status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"message":str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
        