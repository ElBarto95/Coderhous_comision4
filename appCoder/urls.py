from django.urls import path
from .views import eliminar_posteo, editarPosteo, mostrar_posteos, posteosForm, editarProfesor, editarCurso, inicio2, AdminLogoutView,AdminLoginView, eliminar_profesor, mostrar_cursos,mostrar_profesores, buscarCamada, inicio, profesoresForm, estudiantesForm, cursoForm, eliminar_curso, SignUpView


urlpatterns= [
    path('cursos/', cursoForm, name='cursos' ),
    path('estudiantes/', estudiantesForm, name='estudiantes'  ),
    path('profesores/', profesoresForm, name='profesores' ),
    path('', inicio, name='inicio' ),
    path('buscarCamada/', buscarCamada, name='buscarCamada' ),
    path('mostrar_profesores/', mostrar_profesores, name='mostrar_profesores'),
    path('mostrar_cursos/', mostrar_cursos, name='mostrar_cursos'),
    path('eliminar_profesor/ <int:id>', eliminar_profesor, name='eliminar_profesor'),
    path('eliminar_curso/ <int:id>', eliminar_curso, name='eliminar_curso'),
    path('registro/', SignUpView.as_view(), name='SignUpView'),
    path('login/', AdminLoginView.as_view(), name='Login'),
    path('logout/', AdminLogoutView.as_view(), name='Logout'),
    path('inicio2/', inicio2, name='inicio2' ),
    path('editarProfesor/<int:id>/', editarProfesor, name="EditarProfesor"),
    path('editarCurso/<int:id>/', editarCurso, name="EditarCurso"),
    path('posteos/', posteosForm, name='post'),
    path('listaposteos/', mostrar_posteos, name='lista_post'),
    path('eliminar_post/ <int:id>', eliminar_posteo, name='eliminar_posteo'),
    path('editar_post/ <int:id>', editarPosteo, name='editar_posteo')
    ]