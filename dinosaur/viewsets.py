from dinosaur.models import Dinosaur
from rest_framework import viewsets
from .serializers import DinosaurSerializer
#IMPORT YOUR SERIALIZERS

class DinosaurViewSet(viewsets.ModelViewSet):
    serializer_class = DinosaurSerializer
    queryset = Dinosaur.objects.all()
