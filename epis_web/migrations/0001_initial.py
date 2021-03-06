# Generated by Django 2.0.5 on 2018-06-01 05:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alumno',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Areaestudio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('color', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Ciclo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.IntegerField()),
                ('nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=100)),
                ('nombre', models.CharField(max_length=100)),
                ('hora_teorica', models.IntegerField()),
                ('hora_practica', models.IntegerField()),
                ('credito', models.IntegerField()),
                ('area_estudio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='epis_web.Areaestudio')),
                ('ciclo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='epis_web.Ciclo')),
            ],
        ),
        migrations.CreateModel(
            name='Docente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='ImagenProyecto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('url', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='IntegranteProyecto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('integrante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='epis_web.Alumno')),
            ],
        ),
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=100)),
                ('resena', models.CharField(max_length=300)),
                ('foto', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Planestudio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=100)),
                ('nombre', models.CharField(max_length=100)),
                ('resena', models.CharField(max_length=300)),
                ('anio', models.IntegerField()),
                ('credito_practica', models.IntegerField()),
                ('credito_extracurricular', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Proyecto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.CharField(max_length=500)),
                ('asesor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='epis_web.Docente')),
                ('curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='epis_web.Curso')),
            ],
        ),
        migrations.CreateModel(
            name='RequisitoCurso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('curso', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='epis_web.Curso')),
            ],
        ),
        migrations.CreateModel(
            name='TipoCurso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='TipoRequisitoCurso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='requisitocurso',
            name='tipo_requisito',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='epis_web.TipoRequisitoCurso'),
        ),
        migrations.AddField(
            model_name='integranteproyecto',
            name='proyecto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='epis_web.Proyecto'),
        ),
        migrations.AddField(
            model_name='docente',
            name='ciclo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='epis_web.Persona'),
        ),
        migrations.AddField(
            model_name='curso',
            name='docente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='epis_web.Docente'),
        ),
        migrations.AddField(
            model_name='curso',
            name='plan_estudio',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='epis_web.Planestudio'),
        ),
        migrations.AddField(
            model_name='curso',
            name='tipo_curso',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='epis_web.TipoCurso'),
        ),
        migrations.AddField(
            model_name='alumno',
            name='ciclo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='epis_web.Persona'),
        ),
    ]
