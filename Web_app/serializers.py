from .models import Libro
from rest_framework import serializers

class LibroSerializers(serializers.ModelSerializer):
    class Meta:
        model : Libro 
        fields = '__all__'