# Generated by Django 5.0.6 on 2025-06-26 21:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cursos', '0007_alter_cursos_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='cursos',
            name='contacto',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
    ]
