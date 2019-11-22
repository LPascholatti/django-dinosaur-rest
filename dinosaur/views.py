from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from dinosaur.models import Dinosaur
from dinosaur.serializers import DinosaurSerializer
from django.contrib.auth.models import User
from rest_framework import generics
from dinosaur.serializers import UserSerializer

@api_view(['GET', 'POST'])
def dinosaur_list(request, format=None):
    if request.method == 'GET':
        dinosaurs = Dinosaur.objects.all()
        serializer = DinosaurSerializer(dinosaurs, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = DinosaurSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def dinosaur_detail(request, pk, format=None):
    try:
        dinosaur = Dinosaur.objects.get(pk=pk)
    except Dinosaur.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = DinosaurSerializer(dinosaur)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = DinosaurSerializer(dinosaur, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        dinosaur.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
