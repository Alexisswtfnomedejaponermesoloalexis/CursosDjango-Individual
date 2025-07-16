from django.shortcuts import render, redirect
from .models import Cursos, ComentarioContacto
from .forms import ComentarioContactoForm, CursoForm
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
            messages.success(request, '¡Comentario registrado exitosamente!') # Optional: add a success message
            return redirect('Comentarios')        
        else:
            messages.error(request, 'Error al registrar el comentario. Por favor, revisa los campos.')
    form = ComentarioContactoForm() # If GET request or form is not valid, re-render with the form
    return render(request,'cursos/contacto.html',{'form': form})

def comentarios(request):
  
    coments=ComentarioContacto.objects.all().select_related('curso').order_by('-created')
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
    confirmacion= 'cursos/confirmarEliminacion.html'):
    comentario = get_object_or_404(ComentarioContacto, id=id)
    if request.method=='POST':
        comentario.delete()
        comentarios=ComentarioContacto.objects.all()
        return render(request, "cursos/comentario.html",
                      {'comentarios':comentarios})
    return render(request, confirmacion, {'object': comentario})
    

def registrar_curso(request):
    if request.method == 'POST':
        form = CursoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, '¡Curso registrado exitosamente!')
            return redirect('Cursos')
    else:
        form = CursoForm()
    
    return render(request, 'contenido/cursos.html', {'form': form})

def editar_curso(request, codCurso):
    curso = get_object_or_404(Cursos, codCurso=codCurso)
    if request.method == 'POST':
        form = CursoForm(request.POST, request.FILES, instance=curso)
        if form.is_valid():
            form.save()
            messages.success(request, '¡Curso actualizado exitosamente!')
            return redirect('Cursos')
    else:
        form = CursoForm(instance=curso)
    return render(request, 'cursos/formEditarCurso.html', {'form': form, 'curso': curso})

def eliminar_curso(request, codCurso):
    curso = get_object_or_404(Cursos, codCurso=codCurso)
    if request.method == 'POST':
        curso.delete()
        messages.success(request, '¡Curso eliminado exitosamente!')
        return redirect('Cursos')
    return render(request, 'cursos/confirmarEliminacionCurso.html', {'object': curso})

