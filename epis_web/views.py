from django.shortcuts import render

# Se agrega modulos necesarios.
from django.http import HttpResponse

# Create your views here.

APP_NAME='epis_web/'

def index(request):
    return render(request, APP_NAME+'index.html')

def mision_vision(request):
    return render(request, APP_NAME+'mision_vision.html')

def admision(request):
    return render(request, APP_NAME+'admision.html')

def noticias(request):
    return render(request, APP_NAME+'noticias.html')

# Investigacion.

def investigacion(request):
    return render(request, APP_NAME+'investigacion/investigacion.html')

def plan_estudio(request):
    return render(request, APP_NAME+'investigacion/plan_estudio.html')

def plan_estudio_historico(request):
    return render(request, APP_NAME+'investigacion/plan_estudio_historico.html')

def malla_curricular(request):
    return render(request, APP_NAME+'investigacion/malla_curricular.html')

def concurso_proyecto(request):
    return render(request, APP_NAME+'investigacion/concurso_proyecto.html')

def concurso_proyecto_historico(request):
    return render(request, APP_NAME+'investigacion/concurso_proyecto_historico.html')
    