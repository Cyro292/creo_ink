from rest_framework import serializers
from core.models import Board

class BoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Board
        fields = ('name', 'password', 'creation_date', 'users', 'elements', 'objects')

