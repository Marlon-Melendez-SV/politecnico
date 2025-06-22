from django.contrib import admin
from .models import Carrera, Curso

### Register your models here.
#admin.site.register(Carrera)
#admin.site.register(Curso)

### Se comentariaron los despliegues anteriores en el Panel-Admin, para hacer demostracion
### de como se haria algo similar con "decoradores de Python" que comienzan con @
@admin.register(Carrera)
class CarreraAdmin(admin.ModelAdmin):
    list_display=('id_car','nombre_car','fechacreacion_car','telefono_car')
    ordering=('nombre_car','fechacreacion_car')
    search_fields=('nombre_car',)
    #list_editable=('nombre_car',)
    list_filter=('nombre_car','fechacreacion_car')
    list_per_page=10
