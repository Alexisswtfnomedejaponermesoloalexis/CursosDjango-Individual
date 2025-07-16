from django.db import models
from ckeditor.fields import RichTextField

class Cursos(models.Model):
    TURNOS = [
        ('Matutino', 'Matutino'),
        ('Vespertino', 'Vespertino'),
        ('Mixto', 'Mixto'),
    ]

    codCurso = models.CharField(max_length=12,verbose_name="Código del Curso") #Texto corto
    nameCurso = models.TextField(verbose_name="Nombre del Curso") #Texto largo
    turnoCurso = models.CharField(max_length=10, verbose_name="Turno del curso")
    cupo_maximo = models.IntegerField(default=30,verbose_name="Cupo máximo del curso") 
    costo = models.FloatField(default=0.0, verbose_name="Costo del curso") 
    contacto = models.EmailField(null=True, blank=True, verbose_name="Contacto del Curso")
    disponible = models.BooleanField(default=True,verbose_name="¿Se encuentra habilitado el curso?")
    imagen = models.ImageField(null=True,upload_to="fotos",verbose_name="Fotografía del curso")
    created = models.DateTimeField(auto_now_add=True) #Fecha y tiempo
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Curso"

        verbose_name_plural = "Cursos"
        ordering = ["-created"]
        #el menos indica que se ordenara del más reciente al más viejo

    def __str__(self):

        return self.codCurso
        #Indica que se mostrára el nombre como valor en la tabla

class Becas(models.Model):
    id = models.AutoField(primary_key=True,verbose_name="Clave")
    curso = models.ForeignKey(Cursos,
    on_delete=models.CASCADE,verbose_name="Curso")
    created = models.DateTimeField(auto_now_add=True,verbose_name="Registrado")
    coment = RichTextField(verbose_name="Beca a aplicar")

    class Meta:

        verbose_name = "Beca"
        verbose_name_plural = "Becas"
        ordering = ["-created"]

    def __str__(self):

        return self.coment
    
class Actividad(models.Model):
    id_act = models.AutoField(primary_key=True, verbose_name="Clave")
    curso = models.ForeignKey(Cursos, on_delete=models.CASCADE,verbose_name="Curso")
    desc_act = RichTextField(verbose_name="Descripción de la Actividad")
    created = models.DateTimeField(auto_now_add=True,verbose_name="Registrado")

    class Meta:

        verbose_name = "Actividad"
        verbose_name_plural = "Actividades"
        ordering = ["-created"]

    def __str__(self):

        return self.desc_act
    
    
class ComentarioContacto(models.Model):
    id = models.AutoField(primary_key=True,verbose_name="Clave")
    usuario = models.TextField(verbose_name="Usuario")
    mensaje = models.TextField(verbose_name="Comentario")
    created =models.DateTimeField(auto_now_add=True,verbose_name="Registrado")

    class Meta:
        verbose_name = "Comentario Contacto"
        verbose_name_plural = "Comentarios Contactos"
        ordering = ["-created"]

    def __str__(self):
        return self.mensaje
    
    
class Comentario(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="Clave")
    curso = models.ForeignKey(Cursos, on_delete=models.CASCADE, verbose_name="Curso")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Registrado")
    coment = RichTextField(verbose_name="Comentario")

    class Meta:
        verbose_name = 'Comentario'
        verbose_name_plural = 'Comentarios'
        ordering = ['-created']
    
    def __str__(self):
        return self.coment