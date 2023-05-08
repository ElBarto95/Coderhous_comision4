from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Curso(models.Model):

    nombre=models.CharField(max_length=40)
    camada=models.IntegerField()

    def __str__(self) -> str:
        return f' Nombre: {self.nombre} - Camada: {self.camada} '

class Estudiante(models.Model):

    nombre=models.CharField(max_length=40)
    apellido=models.CharField(max_length=40)
    email=models.EmailField()

    def __str__(self) -> str:
        return f' Nombre: {self.nombre} - Apellido: {self.apellido} - Email: {self.email} '

class Profesor(models.Model):

    nombre=models.CharField(max_length=40)
    apellido=models.CharField(max_length=40)
    email=models.EmailField()
    profesion=models.CharField(max_length=40)

    def __str__(self) -> str:
        return f' Nombre: {self.nombre} - Apellido: {self.apellido} - Email: {self.email} - Profecion: {self.profesion}'


class Posteo(models.Model):

    titulo=models.CharField(max_length=30)
    curso_concretado=models.CharField(max_length=40)
    resenia=models.CharField(max_length=200)
    imagen = models.ImageField(upload_to="posts", null=True, blank=True)
    publisher = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name="publisher")
    fecha_post = models.DateField(auto_now_add= True)

    def __str__(self) -> str:
        return f' Titulo: {self.titulo} - curso_concretado: {self.curso_concretado} - resenia: {self.resenia} - imagen: {self.imagen} - fecha_post: {self.fecha_post}'

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='profile_images', blank=True, null=True)

class UsuarioImagen(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='usuarioImagen', null=True, blank = True)
 
    def __str__(self):
        return f"{self.user} - {self.imagen}"

class Mensaje(models.Model):
    mensaje= models.TextField(max_length=1000)
    email = models.EmailField()
    destinatario = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name="destinatario")