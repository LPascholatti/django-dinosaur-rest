from dinosaur.models import Dinosaur
from rest_framework import serializers
from django.contrib.auth.models import User

class DinosaurSerializer(serializers.ModelSerializer):
    class Meta:
      model = Dinosaur
      owner = serializers.ReadOnlyField(source='owner.username')
      fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        dinosaurs = serializers.PrimaryKeyRelatedField(many=True, queryset=Dinosaur.objects.all())
        fields = ['id', 'username', 'dinosaurs']