from django.http import Http404, QueryDict
from rest_framework import permissions, status, generics
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView

from api.serializers import *


class Cards(APIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    parser_classes = (JSONParser,)

    def get_record(self, unique_number):
        try:
            return Card.objects.get(uniqueNumber=unique_number)
        except Card.DoesNotExist:
            raise Http404

    def get(self, request, format=None):
        data = Card.objects.all()
        serializer = CardSerializer(data, many=True)
        return Response(serializer.data)

    def put(self, request, format=None):
        try:
            unique_number = request.data['uniqueNumber']
        except KeyError:
            return Response({'missing field': 'uniqueNumber'}, status=status.HTTP_400_BAD_REQUEST)

        record = self.get_record(unique_number)
        serializer = CardSerializer(record, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request, format=None):
        serializer = CardSerializer(data=request.data)
        # serializer = CardSerializer(data=request.query_params)
        if serializer.is_valid():
            serializer.save(owner=self.request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, format=None):
        try:
            unique_number = request.data['uniqueNumber']
        except KeyError:
            return Response({'missing field': 'uniqueNumber'}, status=status.HTTP_400_BAD_REQUEST)

        record = self.get_record(unique_number)
        record.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CardDetails(APIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    parser_classes = (JSONParser,)

    def get_record(self, cardid):
        try:
            return Card.objects.get(uniqueNumber=cardid)
        except Card.DoesNotExist:
            raise Http404

    def get(self, request, cardid, format=None):
        record = self.get_record(cardid)
        serializer = CardSerializer(record)
        return Response(serializer.data)


# class ArchiveCards(APIView):
#     permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
#     parser_classes = (JSONParser,)
#
#     def get(self, request, format=None):
#         records = Card.objects.filter(archiveStatus=True)
#         serializer = CardSerializer(records, many=True)
#         return Response(serializer.data)
#
#     def post(self, request, format=None):
#         params = dict(request.query_params)
#         if params.get('carduuid', False):
#             record = Card.objects.filter(uniqueNumber=params.get('carduuid')[0])[0]
#             record.archiveStatus = True
#             record.save()
#             print(record.archiveStatus)
#             return Response(status=status.HTTP_201_CREATED)
#         else:
#             return Response(status=status.HTTP_400_BAD_REQUEST)


class Boards(APIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    parser_classes = (JSONParser,)

    def get_record(self, boardId):
        try:
            return Board.objects.get(id=boardId)
        except Board.DoesNotExist:
            raise Http404

    def get(self, request, format=None):
        data = Board.objects.all()
        serializer = BoardSerializer(data, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = BoardSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, format=None):
        try:
            boardId = request.data['id']
        except KeyError:
            return Response({'missing field': 'id'}, status=status.HTTP_400_BAD_REQUEST)

        record = self.get_record(boardId)
        serializer = BoardSerializer(record, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Tables(APIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    parser_classes = (JSONParser,)

    def get_record(self, table_id):
        try:
            return Table.objects.get(id=table_id)
        except Table.DoesNotExist:
            raise Http404

    def get(self, request, format=None):
        data = Table.objects.all()
        serializer = TableSerializer(data, many=True)
        return Response(serializer.data)

    def put(self, request, format=None):
        try:
            id = request.data['id']
        except KeyError:
            return Response({'missing field': 'id'}, status=status.HTTP_400_BAD_REQUEST)

        record = self.get_record(id)
        serializer = TableSerializer(record, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request, format=None):
        serializer = TableSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BoardTables(APIView):
    parser_classes = (JSONParser,)

    def get(self, request, id, format=None):
        records = Table.objects.filter(boardID=id)
        serializer = TableSerializer(records, many=True)
        return Response(serializer.data)


class TableContents(APIView):
    parser_classes = (JSONParser,)

    def get(self, request, tableid, format=None):
        records = Card.objects.filter(tableID=tableid, archiveStatus=False)
        serializer = CardSerializer(records, many=True)
        return Response(serializer.data)


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
