from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('mision_vision', views.mision_vision, name='mision_vision'),


    path('admision', views.admision, name='admision'),


    path('noticias', views.noticias, name='noticias'),

    path('plan_estudio', views.plan_estudio, name='plan_estudio'),
    path('plan_estudio_historico', views.plan_estudio_historico, name='plan_estudio_historico'),

]