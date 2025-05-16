from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Libro(models.Model):
    titulo = models.CharField(max_length=100)
    autor = models.CharField(max_length=100)
    anio = models.IntegerField()
    genero = models.CharField(max_length=100)
    descripcion = models.TextField()

class Resenias(models.Model):
    PUNTAJES = [
        (1, 'Muy Malo'),
        (2, 'Malo'),
        (3, 'Regular'),
        (4, 'Bueno'),
        (5, 'Excelente'),
    ]
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE, null=False )
    usuario = models.ForeignKey(User, null=False, on_delete=models.DO_NOTHING)
    puntaje= models.IntegerField(choices=PUNTAJES)
    comentario=models.TextField()


