from django.urls import path
from .views import  inicio2, AdminLogoutView,AdminLoginView, eliminar_profesor, mostrar_cursos,mostrar_profesores, buscarCamada, inicio, profesoresForm, estudiantesForm, cursoForm, eliminar_curso, SignUpView


urlpatterns= [
    path('cursos/', cursoForm, name='cursos' ),
    path('estudiantes/', estudiantesForm, name='estudiantes'  ),
    path('profesores/', profesoresForm, name='profesores' ),
    path('', inicio, name='inicio' ),
    path('buscarCamada/', buscarCamada, name='buscarCamada' ),
    path('mostrar_profesores/', mostrar_profesores, name='mostrar profesores' ),
    path('mostrar_cursos/', mostrar_cursos, name='mostrar cursos' ),
    path('eliminar_profesor/ <nombre>', eliminar_profesor, name='eliminar_profesor' ),
    path('eliminar_curso/ <nombre>', eliminar_curso, name='eliminar_curso' ),
    path('registro/', SignUpView.as_view(), name='SignUpView' ),
    path('login/', AdminLoginView.as_view(), name='Login' ),
    path('logout/', AdminLogoutView.as_view(), name='Logout' ),
    path('inicio2/', inicio2, name='inicio2' ),

    ]