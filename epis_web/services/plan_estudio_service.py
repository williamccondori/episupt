from epis_web.models import Planestudio, Ciclo, RequisitoCurso

# Constantes del tipo de curso.
CURSO_OBLIGATORIO = 1
CURSO_ELECTIVO = 2
# Constantes del tipo de pre requisito.


class PlanestudioService(object):

    def obtener_requisitos(self, curso_id):
        SIN_REQUISITO = 'Ninguno'
        requisitos = []
        requisitos_set = list(
            RequisitoCurso.objects.filter(curso_id=curso_id).all())
        if len(requisitos_set) == 0:
            requisitos.append({'nombre': SIN_REQUISITO})
        for requisito in requisitos_set:
            if requisito.tipo_requisito_id == 'CR':
                nombre = 'Mín. {} Créditos'.format(requisito.credito)
            else:
                nombre = str(requisito.curso_asignado.codigo)
            requisito = {'nombre': nombre}
            """
            switcher = {
                'CR': ,
                'CU': 
            }
            requisito = {'nombre': switcher.get(requisito.tipo_requisito_id)}
            """
            requisitos.append(requisito)
        return requisitos

    def obtener_ultimo(self):
        plan_estudio = Planestudio.objects.order_by('id').last()
        cursos = list(plan_estudio.curso_set.all())
        for curso in cursos:
            curso.hora_total = curso.hora_teorica + curso.hora_practica
            curso.requisitos = self.obtener_requisitos(curso.id)
        cursos_obligatorios = [
            x for x in cursos if x.tipo_curso_id == CURSO_OBLIGATORIO]
        cursos_electivos = [
            x for x in cursos if x.tipo_curso_id == CURSO_ELECTIVO]
        ciclos = list(Ciclo.objects.all().order_by('id'))
        plan_estudio.credito_obligatorio = sum(
            x.credito for x in cursos_obligatorios)
        plan_estudio.credito_electivo = sum(
            x.credito for x in cursos_electivos)
        plan_estudio.credito_total = (plan_estudio.credito_practica +
                                      plan_estudio.credito_extracurricular +
                                      plan_estudio.credito_obligatorio +
                                      plan_estudio.credito_electivo)
        respuesta = {
            'plan_estudio': plan_estudio,
            'cursos_obligatorios': cursos_obligatorios,
            'cursos_electivos': cursos_electivos,
            'ciclos': ciclos
        }
        return respuesta
