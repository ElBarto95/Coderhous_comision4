from django.shortcuts import redirect, render
from django.http import HttpResponse
from .forms import CursoForm, ProfesorForm, EstudianteForm, SignUpForm
from .models import Curso, Profesor, Estudiante
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView

#from appMVT.forms import
# Create your views here.

def estudiantesForm(request):

      if request.method == 'POST':

            form_estudiante = EstudianteForm(request.POST)

            print(form_estudiante)

            if form_estudiante.is_valid:

                  informacion = form_estudiante.cleaned_data

                  estud_form = Estudiante (
                        nombre=informacion['nombre'], 
                        apellido=informacion['apellido'], 
                        email=informacion['email'], 
                        ) 

                  estud_form.save()

                  return render (request, "index.html")
      else:
            form_estudiante = EstudianteForm()

      return render(request, "estudiante.html", {"form_estudiante":form_estudiante})

def profesoresForm(request):

      if request.method == 'POST':

            form_profesor = ProfesorForm(request.POST)

            print(form_profesor)

            if form_profesor.is_valid:

                  informacion = form_profesor.cleaned_data

                  prof_form = Profesor (
                        nombre=informacion['nombre'], 
                        apellido=informacion['apellido'], 
                        email=informacion['email'], 
                        profesion=informacion['profesion']
                        ) 

                  prof_form.save()

                  return render (request, "index.html")
      else:
            form_profesor = ProfesorForm()

      return render(request, "profesor.html", {"form_profesor":form_profesor})

def cursoForm(request):

      if request.method == 'POST':

            form_curso = CursoForm(request.POST)

            print(form_curso)

            if form_curso.is_valid:

                  informacion = form_curso.cleaned_data

                  curso = Curso (nombre=informacion['curso'], camada=informacion['camada']) 

                  curso.save()

                  return render (request, "index.html")
      else:
            form_curso = CursoForm()

      return render(request, "curso.html", {"form_curso":form_curso})

def inicio(request):

      return render(request, "index.html")

def inicio2(request):

      return render(request, "index2.html")

def buscarCamada(request):

      if request.GET.get('comision', False):

            comision = request.GET['comision']
            cursos = Curso.objects.filter(comision__icontains=comision)

            return render(request, 'buscarCamada.html', {'cursos': cursos})

      else:
            respuesta = 'no se encontro ningun curso con ese numero de comision'
      
      return render(request, 'buscarCamada.html', {'respuesta': respuesta})

def mostrar_profesores(request):

      profesores= Profesor.objects.all()

      context = {'profesores': profesores} 

      return render(request, 'mostrar_profesores.html', context=context)

def mostrar_cursos(request):

      cursos= Curso.objects.all()

      context = {'cursos': cursos} 

      return render(request, 'mostrar_cursos.html', context=context)

def eliminar_profesor(request, profesor_nombre):

      profesor = Profesor.objet.get(nombre= profesor_nombre)
      profesor.delete()

      profesores = Profesor.objects.all()
      context = {'profesores': profesores} 
      
      return render(request, 'mostrar_profesores.html', context=context)

def eliminar_curso(request, curso_nombre):

      curso = Curso.objet.get(nombre= curso_nombre)
      curso.delete()

      cursos = Curso.objects.all()
      context = {'cursos': cursos}
      
      return render(request, 'mostrar_cursos.html', context=context)

class SignUpView(CreateView):

      form_class = SignUpForm
      success_url = reverse_lazy('Login')
      template_name = 'registro.html'

class AdminLoginView(LoginView):
      template_name= 'login.html'

class AdminLogoutView(LogoutView):
      template_name= 'index.html'