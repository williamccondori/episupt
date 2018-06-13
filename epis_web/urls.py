from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('mapa_sitio', views.mapa_sitio, name='mapa_sitio'),
    path('contacto', views.contacto, name='contacto'),


    path('admision', views.admision, name='admision'),

    # Publicaciones.
    path('noticias', views.noticias, name='noticias'),
    path('publicaciones', views.publicaciones, name='publicaciones'),

    # Investigacion.
    path('investigacion', views.investigacion, name='investigacion'),
    path('investigacion/plan_estudio', views.plan_estudio, name='plan_estudio'),
    path('investigacion/plan_estudio_historico', views.plan_estudio_historico, name='plan_estudio_historico'),
    path('investigacion/malla_curricular', views.malla_curricular, name='malla_curricular'),
    path('investigacion/concurso_proyecto', views.concurso_proyecto, name='concurso_proyecto'),
    path('investigacion/concurso_proyecto_historico', views.concurso_proyecto_historico, name='concurso_proyecto_historico'),  
]