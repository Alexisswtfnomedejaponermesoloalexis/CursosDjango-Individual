"""
URL configuration for CursosDjango project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views # Importa las funciones de vistas
from contenido import views
from cursos import views as views_cursos
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('',views_cursos.cursos, name="Principal"),
    #path('', views.principal, name='Principal'), # Página principal
    path('cursos/', views.cursos, name='Cursos'), # Página de cursos disponibles
    path('registrar-curso/', views_cursos.registrar_curso, name='registrar_curso'),
    path('contacto/', views_cursos.contacto, name='Contacto'), # Página de formulario de contacto
    path('registrar/', views_cursos.registrar ,name="Registrar"),
    
    path('comentarios/', views_cursos.comentarios, name="Comentarios"),
    path('formulario/', views.formulario, name='Formulario'),
  path('formEditarComentario/<int:id>/',
         views_cursos.consultarComentarioIndividual, name='ConsultaIndividual'),

    path('editarComentario/<int:id>/',views_cursos.editarComentarioContacto,name='Editar'),
         path('eliminarComentario/<int:id>/',views_cursos.eliminarComentarioContacto,name='Eliminar'),
         
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



