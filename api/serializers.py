from rest_framework import serializers
from django.contrib.auth.models import User
from api.models import Board, Card, Table


class CardSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Card
        fields = ('uniqueNumber', 'archiveStatus', 'title', 'description', 'owner', 'tableID')


class TableSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Table
        fields = ('id', 'tableTitle', 'tableDescription', 'boardID', 'owner')


class BoardSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Board
        fields = ('id', 'boardTitle', 'private_access', 'boardDescription', 'owner')


class UserSerializer(serializers.ModelSerializer):
    boards = serializers.PrimaryKeyRelatedField(many=True, queryset=Board.objects.all())
    tables = serializers.PrimaryKeyRelatedField(many=True, queryset=Table.objects.all())
    cards = serializers.PrimaryKeyRelatedField(many=True, queryset=Card.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'boards', 'tables', 'cards')
