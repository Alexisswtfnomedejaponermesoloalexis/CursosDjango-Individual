from django.shortcuts import render
from .models import Cursos
#Accedemos al modelo Alumnos que contiene la estructura de la tabla.
# Create your views here.
def cursos(request):

    curso=Cursos.objects.all()

#all recupera todos los objetos del modelo (registros de la tabla alumnos)
    return render(request,"cursos/principal.html",{'Cursos':curso})
#Indicamos el lugar donde se renderizará el resultado de esta vista
# y enviamos la lista de alumnos recuparados
# Create your views here.
