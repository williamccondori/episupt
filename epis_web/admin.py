from django.contrib import admin

from epis_web.models import Persona, Ciclo, Areaestudio, TipoCurso, TipoRequisitoCurso, Docente, Alumno
from epis_web.models import Planestudio, Curso, RequisitoCurso, Proyecto, ImagenProyecto, IntegranteProyecto

# Register your models here.

admin.site.register(Persona)
admin.site.register(Ciclo)
admin.site.register(Areaestudio)
admin.site.register(TipoCurso)
admin.site.register(TipoRequisitoCurso)
admin.site.register(Docente)
admin.site.register(Alumno)
admin.site.register(Planestudio)
admin.site.register(Curso)
admin.site.register(RequisitoCurso)
admin.site.register(Proyecto)
admin.site.register(ImagenProyecto)
admin.site.register(IntegranteProyecto)