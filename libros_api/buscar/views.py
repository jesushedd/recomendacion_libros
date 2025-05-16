from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from core.models import Libro
from .serializers import LibroSerializer
from django.shortcuts import get_list_or_404, get_object_or_404

# Create your views here.

def listar_por_genero(request, nombre_genero):
    if request.method == 'GET':
        libros_por_genero =  get_list_or_404(Libro, genero__iexact=nombre_genero)
        serializer = LibroSerializer(libros_por_genero, many=True)
        print(serializer.data)
        return JsonResponse(serializer.data, safe=False)

def listar_por_autor(request, nombre_autor):
    libros_por_autor = get_list_or_404(Libro, autor__iexact = nombre_autor)
    serializer = LibroSerializer(libros_por_autor, many=True)
    return JsonResponse(serializer.data, safe=False)

def detalle(request, id):
    libro = get_object_or_404(Libro, id=id)
    serializer = LibroSerializer(libro)
    return JsonResponse(serializer.data, safe=False)
    
