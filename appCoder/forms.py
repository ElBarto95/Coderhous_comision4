from django import forms
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

class PosteosForm(forms.Form):

    titulo=forms.CharField(max_length=30)
    curso_concretado=forms.CharField(max_length=40)
    resenia=forms.CharField(max_length=200)
    #imagenes