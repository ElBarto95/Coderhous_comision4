from django import forms
from .models import Posteo
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class CursoForm(forms.Form):

    curso = forms.CharField(max_length=40)
    camada = forms.IntegerField()

class ProfesorForm(forms.Form):

    nombre = forms.CharField(max_length=40)
    apellido = forms.CharField(max_length=40)
    email = forms.EmailField()
    profesion = forms.CharField(max_length=40)

class EstudianteForm(forms.Form):

    nombre = forms.CharField(max_length=40)
    apellido = forms.CharField(max_length=40)
    email = forms.EmailField()

class SignUpForm(UserCreationForm):

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password1',
            'password2'
        ]

class UserEditForm(UserCreationForm):

    email = forms.EmailField(label="Ingrese su email:")
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir la contraseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['email', 'password1', 'password2']


class PosteosForm(forms.Form):

    titulo=forms.CharField(max_length=30)
    curso_concretado=forms.CharField(max_length=40)
    resenia=forms.CharField(max_length=200)

    
    class Meta:
        model = Posteo
        fields = ['titulo', 'curso_concretado', 'resenia', 'imagen']