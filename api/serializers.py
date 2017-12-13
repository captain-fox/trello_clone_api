from rest_framework import serializers
from django.contrib.auth.models import User
from api.models import Board, Card, Table


class CardSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Card
        fields = ('archiveStatus', 'title', 'description', 'owner', 'tableID', 'uniqueNumber')


class TableSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Table
        fields = ('tableTitle', 'tableDescription', 'boardID', 'owner')


class BoardSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Board
        fields = ('boardTitle', 'boardDescription', 'owner')


class UserSerializer(serializers.ModelSerializer):
    cards = serializers.PrimaryKeyRelatedField(many=True, queryset=Card.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'boards', 'tables', 'cards')
