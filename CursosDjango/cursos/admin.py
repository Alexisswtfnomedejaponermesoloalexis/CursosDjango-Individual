from django.contrib import admin
from .models import Cursos
from .models import Becas

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