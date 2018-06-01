from epis_web.models import Planestudio

class PlanestudioService(object):
    def obtener_ultimo(self):
        plan_estudio = Planestudio.objects.order_by('id').last()
        print(plan_estudio)
        cursos = plan_estudio.curso_set.all()
        print(cursos)
        return plan_estudio