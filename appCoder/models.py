from django.db import models

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
    
    #imagenes
    def __str__(self) -> str:
        return f' Titulo: {self.titulo} - curso_concretado: {self.curso_concretado} - resenia: {self.resenia}'

