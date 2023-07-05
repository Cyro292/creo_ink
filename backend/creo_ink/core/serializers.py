from rest_framework import serializers
from .models import MyUserModel, Board, Participation

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUserModel
        fields = ['id', 'username', 'email']  # Add other fields as needed

class BoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Board
        fields = ['name', 'slug', 'creation_date', 'elements']  # Add other fields as needed

class UserBoardSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Participation
        fields = ['user', 'permission', 'join_date']  # Add other fields as needed

class BoardPermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Participation
        fields = ['permission']  # Add other fields as needed

# Add the remaining serializers for other models

