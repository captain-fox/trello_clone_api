from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import Http404
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from api.models import Card, Board
from api.serializers import CardSerializer, BoardSerializer


class Cards(APIView):
    def get(self, request, format=None):
        data = Card.objects.all()
        serializer = CardSerializer(data, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CardSerializer(data=request.query_params)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Boards(APIView):
    def get(self, request, format=None):
        data = Board.objects.all()
        serializer = BoardSerializer(data, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = BoardSerializer(data=request.query_params)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BoardDetails(APIView):

    def get(self, request, id, format=None):
        records = Card.objects.filter(boardID=id)
        serializer = CardSerializer(records, many=True)
        return Response(serializer.data)


class CardDetails(APIView):

    def get_record(self, un):
        try:
            return Card.objects.get(uniqueNumber=un)
        except Card.DoesNotExist:
            raise Http404

    def get(self, request, un, format=None):
        record = self.get_record(un)
        serializer = CardSerializer(record)
        return Response(serializer.data)

    def put(self, request, un, format=None):
        record = self.get_record(un)
        serializer = CardSerializer(record, data=request.query_params)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, un, format=None):
        record = self.get_record(un)
        record.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)