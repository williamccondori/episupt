# Generated by Django 2.0.5 on 2018-06-01 05:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('epis_web', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='alumno',
            old_name='ciclo',
            new_name='persona',
        ),
        migrations.RenameField(
            model_name='docente',
            old_name='ciclo',
            new_name='persona',
        ),
    ]
