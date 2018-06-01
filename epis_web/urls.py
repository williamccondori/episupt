from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='web_index'),
    path('mision_vision', views.mision_vision, name='mision_vision'),


    path('admision', views.admision, name='admision'),


    path('noticias', views.noticias, name='noticias'),

    # Investigacion.
    path('investigacion', views.investigacion, name='investigacion'),
    path('investigacion/plan_estudio', views.plan_estudio, name='plan_estudio'),
    path('investigacion/plan_estudio_historico', views.plan_estudio_historico, name='plan_estudio_historico'),
    path('investigacion/malla_curricular', views.malla_curricular, name='malla_curricular'),
    path('investigacion/concurso_proyecto', views.concurso_proyecto, name='concurso_proyecto'),
    path('investigacion/concurso_proyecto_historico', views.concurso_proyecto_historico, name='concurso_proyecto_historico'),  
]