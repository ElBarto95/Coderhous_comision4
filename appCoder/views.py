from django.shortcuts import redirect, render
from django.http import HttpResponse
from .forms import CursoForm, ProfesorForm, EstudianteForm, SignUpForm, PosteosForm, UserEditForm
from .models import Curso, Profesor, Estudiante, Posteo, UsuarioImagen
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

      if request.GET.get('camada', False):

            camada = request.GET['camada']
            cursos = Curso.objects.filter(camada__icontains=camada)

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

    profesor = Profesor.objects.get(id=id)

    if request.method == 'POST':

        miFormulario = ProfesorForm(request.POST)

        if miFormulario.is_valid():

            informacion = miFormulario.cleaned_data

            profesor.nombre = informacion['nombre']
            profesor.apellido = informacion['apellido']
            profesor.email = informacion['email']
            profesor.profesion = informacion['profesion']

            profesor.save()

            return render(request, "index.html")
    else:

        miFormulario = ProfesorForm(initial={'nombre': profesor.nombre, 'apellido': profesor.apellido,'email': profesor.email, 'profesion': profesor.profesion})

    return render(request, "editarProfesor.html", {"miFormulario": miFormulario, "profesor_nombre": profesor.nombre})

def editarCurso(request, id):

    curso = Curso.objects.get(id=id)

    if request.method == 'POST':

       
        miFormulario = CursoForm(request.POST)

        if miFormulario.is_valid():

            informacion = miFormulario.cleaned_data

            curso.curso = informacion['curso']
            curso.camada = informacion['camada']
           
            curso.save()
            return render(request, "index.html")
    else:
        # Creo el formulario con los datos que voy a modificar
        miFormulario = CursoForm(initial={'curso': curso.nombre, 'camada': curso.camada,})

   
    return render(request, "editarCurso.html", {"miFormulario": miFormulario, "curso_nombre": id})

def posteosForm(request):

      if request.method == 'POST':

            form_posteo = PosteosForm(request.POST, request.FILES)

            print(form_posteo)

            if form_posteo.is_valid:

                  informacion = form_posteo.cleaned_data

                  post_form = Posteo (
                        titulo=informacion['titulo'], 
                        curso_concretado=informacion['curso_concretado'], 
                        resenia=informacion['resenia'], 
                        imagen = informacion['imagen']
                        ) 

                  post_form.save()

                  return render (request, "index.html")
      else:
            form_posteo = PosteosForm()

      return render(request, "posteos.html", {"form_posteo":form_posteo})

def mostrar_posteos(request):

      posteos= Posteo.objects.all()

      context = {'posteos': posteos} 

      return render(request, 'mostrar_posteos.html', context=context)

@login_required
def eliminar_posteo(request, id):

      posteo = Posteo.objects.get(id=id)
      posteo.delete()

      posteos = Posteo.objects.all()
      context = {'posteos': posteos} 
      
      return render(request, 'mostrar_posteos.html', context=context)

@login_required
def editarPosteo(request, id):

    posteos = Posteo.objects.get(id=id)

    if request.method == 'POST':

        miFormulario = PosteosForm(request.POST)

        if miFormulario.is_valid():

            informacion = miFormulario.cleaned_data

            posteos.titulo = informacion['titulo']
            posteos.curso_concretado = informacion['curso_concretado']
            posteos.resenia = informacion['resenia']

           
            posteos.save()
            return render(request, "index.html")
    else:

        miFormulario = PosteosForm(initial={'titulo': posteos.titulo, 'curso_concretado': posteos.curso_concretado,})

   
    return render(request, "editarPosteo.html", {"miFormulario": miFormulario, "posteo_titulo": id})

@login_required
def editarPerfil(request):

    usuario = request.user

    if request.method == 'POST':

        miFormulario = UserEditForm(request.POST)

        if miFormulario.is_valid():

            informacion = miFormulario.cleaned_data

            usuario.email = informacion['email']
            usuario.password1 = informacion['password1']
            usuario.password2 = informacion['password2']

            usuario.save()

            return render(request, "index2.html")

    else:

        miFormulario = UserEditForm(initial={'email': usuario.email})

    return render(request, "editarPerfil.html", {"miFormulario": miFormulario, "usuario": usuario})

def about(request):
     return render(request, 'about.html')
