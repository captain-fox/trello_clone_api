from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import Http404
from rest_framework.parsers import JSONParser

from rest_framework.views import APIView
from api.models import Card, Table, Board
from api.serializers import CardSerializer, TableSerializer, BoardSerializer


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
        params = dict(request.query_params)
        print(params.get('provider', False), params.get('uuid', False))
        data = Board.objects.all()
        serializer = BoardSerializer(data, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = BoardSerializer(data=request.query_params)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Tables(APIView):
    def get(self, request, format=None):
        data = Table.objects.all()
        serializer = TableSerializer(data, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = TableSerializer(data=request.query_params)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BoardTables(APIView):
    def get(self, request, id, format=None):
        records = Table.objects.filter(boardID=id)
        serializer = TableSerializer(records, many=True)
        return Response(serializer.data)


class TableContents(APIView):
    def get(self, request, tableid, format=None):
        records = Card.objects.filter(tableID=tableid)
        serializer = CardSerializer(records, many=True)
        return Response(serializer.data)


class CardDetails(APIView):
    def get_record(self, cardid):
        try:
            return Card.objects.get(uniqueNumber=cardid)
        except Card.DoesNotExist:
            raise Http404

    def get(self, request, cardid, format=None):
        record = self.get_record(cardid)
        serializer = CardSerializer(record)
        return Response(serializer.data)

    def put(self, request, cardid, format=None):
        record = self.get_record(cardid)
        serializer = CardSerializer(record, data=request.query_params)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, cardid, format=None):
        record = self.get_record(cardid)
        record.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)