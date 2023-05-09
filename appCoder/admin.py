from django.contrib import admin
from .models import Curso, Estudiante, Profesor, Posteo, UsuarioImagen, Profile, Mensaje
# Register your models here.
admin.site.register(Curso)
admin.site.register(Estudiante)
admin.site.register(Profesor)
admin.site.register(Posteo)
admin.site.register(UsuarioImagen)
admin.site.register(Profile)
admin.site.register(Mensaje)
