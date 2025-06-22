from django.urls import path
##from . import views  ## Cambio debido ala nueva carpeta views para views.py
#from .views.views import inicio
from Aplicaciones.Educacion.views.views import inicio
from Aplicaciones.Educacion.views.views import (
    inicio,
    carreras,
    htmx1,
    mensaje_view,
    crear_carrera,
    eliminar_carrera,
    editar_carrera,
    procesar_editar_carrera
)

from Aplicaciones.Educacion.views.curso_views import (
    cursos,
    crear_curso,
    eliminar_curso,
    curso_editar,
    procesar_editar_curso
)

from Aplicaciones.Educacion.views.correo_views import (
    correo,
    enviar_correo,
    enviar_correo_dos
)

urlpatterns=[
    path('',inicio), 
    ### URLs para Carreras
    path('carreras/',carreras,name='carreras'),
    path('mensaje/', mensaje_view, name='mensaje'),  # Nueva
    path('crear_carrera/',crear_carrera, name="crear_carrera"),  ## IMPORTANTE: Este "name" es el que pondra en el "action" del formulario usando jinja
    path('eliminar_carrera/<id>',eliminar_carrera, name='eliminar_carrera'),
    path('editar_carrera/<id>', editar_carrera, name='editar_carrera'),
    path('procesar_editar_carrera/', procesar_editar_carrera, name='procesar_editar_carrera'),

    ### URLs para Cursos
    path('cursos/',cursos, name='cursos'),
    path('crear_curso/',crear_curso, name="crear_curso"),  ## IMPORTANTE: Este "name" es el que pondra en el "action" del formulario usando jinja
    path('eliminar_curso/<id>',eliminar_curso, name='eliminar_curso'),
    path('curso_editar/<id>', curso_editar, name='curso_editar'),
    path('procesar_editar_curso/', procesar_editar_curso, name='procesar_editar_curso'),

   ## URL para Correo
   path('correo/',correo, name='correo'),
   path('enviar_correo/', enviar_correo, name='enviar_correo'),
   path('enviar_correo_dos/', enviar_correo_dos, name='enviar_correo_dos'),

    ### para HTMX
     path('htmx1/',htmx1),

]