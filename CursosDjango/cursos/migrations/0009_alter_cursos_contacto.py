# Generated by Django 5.0.6 on 2025-06-26 21:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cursos', '0008_cursos_contacto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cursos',
            name='contacto',
            field=models.EmailField(blank=True, max_length=254, null=True, verbose_name='Contacto del Curso'),
        ),
    ]
