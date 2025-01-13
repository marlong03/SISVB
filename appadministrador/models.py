from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.utils.timezone import now
class Rol(models.Model):
    name = models.CharField(max_length=100)
    state = models.IntegerField(default=1)
    
    def __str__(self):
        return self.nombre

class Usuario(AbstractUser):
    document_number = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)  # Auto asigna la fecha de creación
    date_modified = models.DateTimeField(auto_now=True)
    id_rol = models.ForeignKey(Rol, related_name='id_rol', on_delete=models.DO_NOTHING,default=3)

    def __str__(self):
        return self.username

class TipoVotacion(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    number_votes = models.IntegerField(default=0)
    date_created = models.DateTimeField(auto_now_add=True)  # Auto asigna la fecha de creación
    date_modified = models.DateTimeField(auto_now=True)
    state = models.IntegerField(default=1)
    date_start = models.DateTimeField(default=now) # Falta modificar
    date_end = models.DateTimeField(default=now) # Falta modificar

    def __str__(self):
        return self.name

class Plancha(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.TextField()
    state = models.IntegerField(default=1)
    date_created = models.DateTimeField(auto_now_add=True)  # Auto asigna la fecha de creación
    date_modified = models.DateTimeField(auto_now=True)
    id_tipovotacion = models.ForeignKey(TipoVotacion, related_name='id_tipovotacion', on_delete=models.DO_NOTHING, default=1)

    def __str__(self):
        return self.name

class Voto(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.DO_NOTHING)
    id_tipovotacion = models.ForeignKey(TipoVotacion, on_delete=models.DO_NOTHING)
    id_plancha = models.ForeignKey(Plancha, on_delete=models.DO_NOTHING)
    date_created = models.DateTimeField(auto_now_add=True)  # Auto asigna la fecha de creación
    date_modified = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('usuario', 'id_plancha', 'id_tipovotacion')

    def __str__(self):
        return f"{self.usuario.name} votó por {self.id_plancha.name}"
