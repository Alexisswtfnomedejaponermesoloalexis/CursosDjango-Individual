from django.contrib import admin
from .models import Cursos
from .models import Becas, Comentario
from .models import Actividad, ComentarioContacto

class AdministrarModelo(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('codCurso', 'nameCurso', 'turnoCurso', 'disponible', 'cupo_maximo')
    search_fields = ('codCurso','nameCurso','turnoCurso')
    date_hierarchy = 'created'
    list_filter = ('codCurso','nameCurso', 'turnoCurso', 'disponible')
   


admin.site.register(Cursos, AdministrarModelo)


class AdministrarBecas(admin.ModelAdmin):
    list_display = ('id', 'coment')
    search_fields = ('id','created')
    date_hierarchy = 'created'
    readonly_fields = ('created', 'id')

    

admin.site.register(Becas, AdministrarBecas)

class AdministrarActividad(admin.ModelAdmin):
    list_display = ('id_act', 'desc_act')
    search_fields = ('id_act','created')
    date_hierarchy = 'created'
    readonly_fields = ('created', 'id_act')
    list_filter = ('id_act', 'created')
admin.site.register(Actividad, AdministrarActividad)

class AdministarComentarios(admin.ModelAdmin):
    list_display = ('id', 'coment')
    search_fields = ('id', 'created')
    date_hierarchy = 'created'
    readonly_fields = ('created', 'id')

admin.site.register(Comentario, AdministarComentarios)


class AdministrarComentariosContacto(admin.ModelAdmin):
    list_display = ('id', 'mensaje')
    search_fields = ('id','created')
    date_hierarchy = 'created'
    readonly_fields = ('created', 'id')

admin.site.register(ComentarioContacto, AdministrarComentariosContacto)
