from django.shortcuts import render, redirect
from .models import Cursos, ComentarioContacto
from .forms import ComentarioContactoForm
from django.contrib import messages
from django.shortcuts import get_object_or_404


#Accedemos al modelo Alumnos que contiene la estructura de la tabla.
# Create your views here.
def cursos(request):

    curso=Cursos.objects.all()

#all recupera todos los objetos del modelo (registros de la tabla alumnos)
    return render(request,"cursos/principal.html",{'Cursos':curso})
#Indicamos el lugar donde se renderizará el resultado de esta vista
# y enviamos la lista de alumnos recuparados
# Create your views here.


def registrar(request):
    if request.method == 'POST':
        form = ComentarioContactoForm(request.POST)
        if form.is_valid(): #Si los datos recibidos son correctos
            form.save() #inserta
            
            return redirect('Comentarios')        
    form = ComentarioContactoForm()
#Si algo sale mal se reenvian al formulario los datos ingresados
    return render(request,'cursos/contacto.html',{'form': form})

def comentarios(request):
    coments=ComentarioContacto.objects.all()
    return render(request, "cursos/comentario.html", {'comentarios':coments})


def contacto(request):
    form = ComentarioContactoForm()
    return render(request,"cursos/contacto.html", {'form': form})
#Indicamos el lugar donde se renderizará el resultado de esta vista

def consultarComentarioIndividual(request, id):
    comentario=ComentarioContacto.objects.get(id=id)

    return render(request, "cursos/formEditarComentario.html", 
        {'comentario':comentario})

def editarComentarioContacto(request, id):
    comentario = get_object_or_404(ComentarioContacto, id=id)
    form = ComentarioContactoForm(request.POST, instance=comentario)

    if form.is_valid():
        form.save()
        comentarios=ComentarioContacto.objects.all()
        return render(request, "cursos/comentario.html",
        {'comentarios': comentarios})
    

    return render(request, "cursos/formEditarComentario.html", 
    {'comentario': comentario})

def eliminarComentarioContacto(request, id,
    confirmacion= 'registros/confirmarEliminacion.html'):
    comentario = get_object_or_404(ComentarioContacto, id=id)
    if request.method=='POST':
        comentario.delete()
        comentarios=ComentarioContacto.objects.all()
        return render(request, "cursos/comentario.html",
                      {'comentarios':comentarios})
    return render(request, confirmacion, {'object': comentario})

