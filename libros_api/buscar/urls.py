from . import views
from django.urls import path
from . import views

app_name = 'buscar'

urlpatterns = [
    #buscar/genero/{nombre_genero}
    path('genero/<str:nombre_genero>', views.listar_por_genero ),
    #buscar/autor/{nombre_author}
    path('autor/<str:nombre_autor>', views.listar_por_autor),
    #buscar por id
    path('<int:id>', views.detalle )
]