from dinosaur.models import Dinosaur
from rest_framework import viewsets

# #IMPORT YOUR SERIALIZERS
from .serializers import *

class DinosaurViewSet(viewsets.ModelViewSet):
  serializer_class = DinosaurSerializer