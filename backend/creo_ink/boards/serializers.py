from rest_framework import serializers
from .models import Board, Participation

class BoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Board
        fields = "__all__"

class BoardMembershipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Participation
        fields = "__all__"
        read_only_fields = ["__all__"]

class UserSettingsUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Participation
        fields = ["settings"]
        
class ParticipationStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Participation
        fields = ['status']

class JoinBoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Participation
        fields = []

class LeaveBoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Participation
        fields = []