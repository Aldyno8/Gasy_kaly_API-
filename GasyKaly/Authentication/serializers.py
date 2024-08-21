from rest_framework import serializers
from django.contrib.auth.models import User
class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fieds = ['username', 'email', 'password']