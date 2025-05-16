from rest_framework import serializers
#from django.contrib.auth.models import Group, User
from core.models import Libro

class LibroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Libro
        fields = [
            'id', 'titulo', 'autor', 'anio', 'genero', 'descripcion'
        ]