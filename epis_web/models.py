from django.db import models

# Create your models here.

class Persona(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    resena = models.CharField(max_length=300)
    foto = models.CharField(max_length=300)

    def __str__(self):
        return self.nombre + ' ' + self.apellido

class Ciclo(models.Model):
    numero = models.IntegerField()
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Areaestudio(models.Model):
    nombre = models.CharField(max_length=100)
    color = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class TipoCurso(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class TipoRequisitoCurso(models.Model):
    nombre = models.CharField(max_length=100)

class Docente(models.Model):
    persona = models.ForeignKey(Persona, on_delete=models.CASCADE)

    def __str__(self):
        return self.persona.nombre + ' ' + self.persona.apellido

class Alumno(models.Model):
    persona = models.ForeignKey(Persona, on_delete=models.CASCADE)

class Planestudio(models.Model):
    codigo = models.CharField(max_length=100)
    nombre = models.CharField(max_length=100)
    resena = models.CharField(max_length=300)
    anio = models.IntegerField()
    credito_practica = models.IntegerField()
    credito_extracurricular = models.IntegerField()

    def __str__(self):
        return self.nombre

class Curso(models.Model):
    codigo = models.CharField(max_length=100)
    nombre = models.CharField(max_length=100)
    ciclo = models.ForeignKey(Ciclo, on_delete=models.CASCADE)
    hora_teorica = models.IntegerField()
    hora_practica = models.IntegerField()
    credito = models.IntegerField()
    plan_estudio = models.ForeignKey(Planestudio, on_delete=models.CASCADE)
    area_estudio = models.ForeignKey(Areaestudio, on_delete=models.CASCADE)
    tipo_curso = models.ForeignKey(TipoCurso, on_delete=models.CASCADE)
    docente = models.ForeignKey(Docente, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

class RequisitoCurso(models.Model):
    tipo_requisito = models.ForeignKey(TipoRequisitoCurso, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, null=True)

class Proyecto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=500)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    asesor = models.ForeignKey(Docente, on_delete=models.CASCADE)

class ImagenProyecto(models.Model):
    nombre = models.CharField(max_length=100)
    url = models.CharField(max_length=300)

class IntegranteProyecto(models.Model):
    integrante = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE)
