from dinosaur.models import Dinosaur
from rest_framework import serializers
from django.contrib.auth.models import User

class DinosaurSerializer(serializers.ModelSerializer):
    class Meta:
      model = Dinosaur
      fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    dinosaurs = serializers.PrimaryKeyRelatedField(many=True, queryset=Dinosaur.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'snippets']