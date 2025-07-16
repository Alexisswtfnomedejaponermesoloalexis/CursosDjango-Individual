from django.shortcuts import render

# Create your views here.

from django.shortcuts import HttpResponse

def principal(request):
    return render(request, 'contenido/principal.html')

def cursos(request):
    return render(request, 'contenido/cursos.html')

def contacto(request):
    return render(request, 'contenido/contacto.html')

def formulario(request):
    contenido = """<h2>Registrar </h2>
    <p>Matricula:<input type="text" name="matricula"></p>
    <p>Nombre:<input type="text" name="nombre"></p>
    <p>Carrera:
    <select name="carrera">
        <option>ING. DGS</option>
        <option>ING. EVND</option>
    <select>
    </p>
    <input type="radio" name"turno" value="matutino">Matutino
    <input type="radio" name"turno" value="vespertino">Vespertino
    <p><input type="Button" name="enviar" value="Enviar"></p>
    """
    return render(request, 'contenido/formulario.html', {'contenido': contenido})



