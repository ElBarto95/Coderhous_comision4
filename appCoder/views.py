from django.shortcuts import redirect, render
from django.http import HttpResponse
from .forms import CursoForm, ProfesorForm, EstudianteForm, SignUpForm, PosteosForm
from .models import Curso, Profesor, Estudiante, Posteo
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

# Create your views here.y

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

def eliminar_profesor(request, id):

      profesor = Profesor.objects.get(id=id)
      profesor.delete()

      profesores = Profesor.objects.all()
      context = {'profesores': profesores} 
      
      return render(request, 'mostrar_profesores.html', context=context)

def eliminar_curso(request, id):

      curso = Curso.objects.get(id=id)
      curso.delete()

      cursos = Curso.objects.all()
      context = {'cursos': cursos}
      
      return render(request, 'mostrar_cursos.html', context=context)

class SignUpView(CreateView):

      form_class = SignUpForm
      success_url = reverse_lazy('Login')
      template_name = 'registro.html'

class AdminLoginView(LoginView):
      success_url = reverse_lazy('inicio2')
      template_name= 'login.html'

class AdminLogoutView(LogoutView):
      template_name= 'index.html'

def editarProfesor(request, id):

    # Recibe el nombre del profesor que vamos a modificar
    profesor = Profesor.objects.get(id=id)

    # Si es metodo POST hago lo mismo que el agregar
    if request.method == 'POST':

        # aquí mellega toda la información del html
        miFormulario = ProfesorForm(request.POST)

        if miFormulario.is_valid:  # Si pasó la validación de Django

            informacion = miFormulario.cleaned_data

            profesor.nombre = informacion['nombre']
            profesor.apellido = informacion['apellido']
            profesor.email = informacion['email']
            profesor.profesion = informacion['profesion']

            profesor.save()

            # Vuelvo al inicio o a donde quieran
            return render(request, "AppCoder/inicio.html")
    # En caso que no sea post
    else:
        # Creo el formulario con los datos que voy a modificar
        miFormulario = ProfesorForm(initial={'nombre': profesor.nombre, 'apellido': profesor.apellido,
                                                   'email': profesor.email, 'profesion': profesor.profesion})

    # Voy al html que me permite editar
    return render(request, "AppCoder/editarProfesor.html", {"miFormulario": miFormulario, "profesor_nombre": profesor.nombre})

def editarCurso(request, id):

    # Recibe el nombre del profesor que vamos a modificar
    profesor = Curso.objects.get(id=id)

    # Si es metodo POST hago lo mismo que el agregar
    if request.method == 'POST':

        # aquí mellega toda la información del html
        miFormulario = CursoForm(request.POST)

        print(miFormulario)

        if miFormulario.is_valid:

            informacion = miFormulario.cleaned_data

            curso.curso = informacion['curso']
            curso.camada = informacion['camada']
           
            curso.save()
            return render(request, "AppCoder/inicio.html")
    else:
        # Creo el formulario con los datos que voy a modificar
        miFormulario = ProfesorForm(initial={'curso': curso.nombre, 'camada': curso.camada,
                                                   'email': profesor.email, 'profesion': profesor.profesion})

    # Voy al html que me permite editar
    return render(request, "AppCoder/editarProfesor.html", {"miFormulario": miFormulario, "profesor_nombre": id})

def posteosForm(request):

      if request.method == 'POST':

            form_posteo = PosteosForm(request.POST)

            print(form_posteo)

            if form_posteo.is_valid:

                  informacion = form_posteo.cleaned_data

                  post_form = Posteo (
                        titulo=informacion['titulo'], 
                        curso_concretado=informacion['curso_concretado'], 
                        resenia=informacion['resenia'], 
                        ) 

                  post_form.save()

                  return render (request, "index.html")
      else:
            form_posteo = PosteosForm()

      return render(request, "posteos.html", {"form_posteo":form_posteo})

class listaPosteo(ListView):
      model = Posteo
      context_object_name = "posteos"
