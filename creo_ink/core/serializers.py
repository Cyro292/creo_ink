from rest_framework import serializers
from core.models import Board, MyUserModel


class BoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Board
        fields = ('name', 'elements')

class BoardRestrictedOverviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Board
        fields = ('name', 'elements')

class BoardOverviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Board
        fields = ('name', 'creation_date', 'users')
        
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUserModel
        fields = ('name', 'creation_date', 'users')

class UserBoardOverviewSerializer(serializers.ModelSerializer):
    boards = BoardOverviewSerializer(many=True, read_only=True)

    def to_representation(self, instance):
        user: MyUserModel = instance
        boards = user.boards.all()
        return {'boards': self.fields['boards'].to_representation(boards)}

    class Meta:
        model = MyUserModel
        fields = ('boards',)
