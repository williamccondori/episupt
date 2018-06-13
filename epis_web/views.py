from django.shortcuts import render

# Se agrega modulos necesarios.
from django.http import HttpResponse

from epis_web.services.plan_estudio_service import PlanestudioService

# Create your views here.

APP_NAME = 'epis_web/'

def index(request): return render(request, APP_NAME+'index.html')
def mapa_sitio(request): return render(request, APP_NAME+'mapa_sitio.html')
def contacto(request): return render(request, APP_NAME+'contacto.html')


def mision_vision(request): return render(request, APP_NAME+'mision_vision.html')
def admision(request): return render(request, APP_NAME+'admision.html')

# Publicacion.
def publicaciones(request): return render(request, APP_NAME+'publicacion/publicaciones.html')
def publicacion(request): return render(request, APP_NAME+'publicacion/publicacion.html')
def noticias(request): return render(request, APP_NAME+'publicacion/noticias.html')
def noticia(request): return render(request, APP_NAME+'publicacion/noticia.html')
    
# Investigacion.
def investigacion(request): return render(request, APP_NAME+'investigacion/investigacion.html')
def plan_estudio(request):
    plan_estudio_service = PlanestudioService()
    respuesta = plan_estudio_service.obtener_ultimo()
    return render(request, APP_NAME+'investigacion/plan_estudio.html', respuesta)
def plan_estudio_historico(request):
    return render(request, APP_NAME+'investigacion/plan_estudio_historico.html')
def malla_curricular(request):
    return render(request, APP_NAME+'investigacion/malla_curricular.html')
def concurso_proyecto(request):
    return render(request, APP_NAME+'investigacion/concurso_proyecto.html')
def concurso_proyecto_historico(request):
    return render(request, APP_NAME+'investigacion/concurso_proyecto_historico.html')
