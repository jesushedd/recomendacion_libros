from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from .models import Libro
from  django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import redirect_to_login
from .helpers import check_user_logged
# Create your views here.

def pag_principal(request):
    if request.method == 'GET':
        catalogo = Libro.objects.all()[:5]

        context = check_user_logged(request)
        context['catalogo'] = catalogo
        return render(request, "core/index.html", context)
def registro(request):
    if request.method == 'GET':
        context = check_user_logged(request)
        return render(request, "core/registro.html", context)
    if request.method == 'POST':
        nombre = request.POST['nombre']
        apellido = request.POST['apellido']
        email = request.POST['email']
        passwd = request.POST['password']

        creando_usuario = User.objects.create_user(email, 
                                              email, 
                                              passwd)
        creando_usuario.first_name = nombre
        creando_usuario.last_name = apellido
        creando_usuario.save()
    
        return HttpResponseRedirect("/")

def login_user(request):
    if request.method == 'GET':
        context = check_user_logged(request)
        if request.user.is_authenticated:
            return HttpResponseRedirect("/")  # or "/"
        return render(request, 'core/login.html', context)
    if request.method == 'POST':

        



        username = request.POST['email']
        passwd = request.POST['password']

        user = authenticate(request, username=username, password=passwd)
        
        if user is not None:
            login(request, user)
            return HttpResponseRedirect("/")
        else:
            context = {
                'error_message' : 1
            }

            return render(request, 'core/login.html', context)

    
def logout_user(request):
    context = check_user_logged(request)
    logout(request)
    return render(request, 'core/logout.html', context)


def clubes(request):
    
    if request.method == 'GET':
        context = check_user_logged(request)
        return render(request, 'core/clubes.html', context)
    
def desc(request, libro_id):
    if request.method == 'GET':
        context = check_user_logged(request)
        libro = get_object_or_404(Libro, pk=libro_id)
        context['libro'] = libro
        return render(request, 'core/libro.html', context)

def calificar(request, libro_id):
    if not request.user.is_authenticated:
        return HttpResponseRedirect("/login")
    if request.method == 'GET':
        libro = get_object_or_404(Libro, pk=libro_id)
        context = check_user_logged(request)
        context['libro'] = libro
        return render(request, "core/calificar.html", context)
    if request.method == 'POST':
        pass
    
        