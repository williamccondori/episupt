# Generated by Django 2.0.5 on 2018-06-02 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('epis_web', '0009_proyecto_categoria'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proyecto',
            name='resena',
            field=models.TextField(),
        ),
    ]
