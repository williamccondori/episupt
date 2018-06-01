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

def plan_estudio(request):
    return render(request, APP_NAME+'plan_estudio.html')