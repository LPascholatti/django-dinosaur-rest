from dinosaur.models import Dinosaur
from rest_framework import viewsets
from .serializers import DinosaurSerializer
#IMPORT YOUR SERIALIZERS

class DinosaurViewSet(viewsets.ModelViewSet):
    queryset = Dinosaur.objects.all()
    serializer_class = DinosaurSerializer
