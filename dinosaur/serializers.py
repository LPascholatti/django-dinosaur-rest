from dinosaur.models import Dinosaur
from rest_framework import serializers

class DinosaurSerializer(serializers.ModelSerializer):
    class Meta:
      model = Dinosaur
      fields = '__all__'