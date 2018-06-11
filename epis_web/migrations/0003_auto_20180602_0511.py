# Generated by Django 2.0.5 on 2018-06-02 05:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('epis_web', '0002_auto_20180601_0523'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requisitocurso',
            name='curso',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='epis_web.Curso'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='requisitocurso',
            name='nombre',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='tiporequisitocurso',
            name='id',
            field=models.CharField(max_length=2, primary_key=True, serialize=False),
        ),
    ]