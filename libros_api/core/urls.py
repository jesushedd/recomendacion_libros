from django.urls import path
from django.shortcuts import render
from . import views
app_name = 'core'
urlpatterns= [
    #pagina principal / --> index
    path("", views.pag_principal ,name='index'),
    #pagina para registarase /registro
    path("registro", views.registro, name='registro'),
    #pagina para login /login
    path("login", views.login_user, name='login'),
    #pagina  /clubes
    path("clubes", views.clubes),
    #link a un libro especifico /libro_id
    path("libro/<int:libro_id>", views.desc),
    #path logout
    path("logout", views.logout_user),
    #path /calificar/id_libro
    path("calificar/<int:libro_id>", views.calificar, name="calificar")
    

]