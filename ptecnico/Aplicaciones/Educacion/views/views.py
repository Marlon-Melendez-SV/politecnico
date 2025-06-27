from django.shortcuts import render,HttpResponse, redirect
#from ..models import Carrera
from Aplicaciones.Educacion.models import Carrera 
from django.contrib import messages
from django.db.models import ProtectedError

## Se importara la libreria auth.decorator "decoradores" para proteger las paginas y que no sean accesadas  
##   sin haberse logueado primero
from django.contrib.auth.decorators import login_required


@login_required(login_url="/login/")
def inicio(request):
    return  render(request,'index.html')


def carreras(request):
    carreras_db=Carrera.objects.all()
    return render(request,'carreras.html',{'carreras_db':carreras_db} )


def crear_carrera(request):
    if request.method=='POST':
        nombre=request.POST['nombre_car']
        fecha_creacion=request.POST['fechacreacion_car']
        telefono=request.POST['telefono_car']
        logo=request.FILES.get('logo_car')
    
        ### comando ORM (object Relational Mapping) para guardar nuevo registro
        Carrera.objects.create(nombre_car=nombre, fechacreacion_car=fecha_creacion, telefono_car=telefono, logo_car=logo)
        messages.success(request, "Carrera creada correctamente.")

        ## Hacer un redirect para actualizar la tabla de carreras
        return redirect('/carreras')


def eliminar_carrera(request, id):
    try:
        carreraDB=Carrera.objects.get(id_car=id)
        carreraDB.delete()
        messages.success(request,"Carrera borrada correctamente.")
    except ProtectedError:
        messages.error(request, "No se puede eliminar la carrera porque tiene cursos asociados.")
    
    return redirect('/carreras')


def editar_carrera(request, id):
    carreraDB=Carrera.objects.get(id_car=id)
    return render(request, 'editar_carrera.html',{'carrera':carreraDB})


def procesar_editar_carrera(request):
       if request.method=='POST':
          id=request.POST['id_car']
          nombre=request.POST['nombre_car']
          fecha_creacion=request.POST['fechacreacion_car']
          telefono=request.POST['telefono_car']
          logotipo=request.FILES.get('logo_car')

          ### Hay que obtener el registro y luego actualizar
          carrera_editar=Carrera.objects.get(id_car=id)
          carrera_editar.nombre_car=nombre
          carrera_editar.fechacreacion_car=fecha_creacion
          carrera_editar.telefono_car=telefono
          if logotipo is not None:
              carrera_editar.logo_car=logotipo

          ## Guardar los cambios (equivalente al update)
          carrera_editar.save()
          messages.success(request,"Carrera actualizada correctamente.")
          return redirect('/carreras')
 

def pagina_no_encontrada(request, exception):
    return render(request, '404.html', status=404)


        
###### Codigo para trabajar con ejemplo HTMX
def htmx1(request):
    return render(request,'boton.html')

def mensaje_view(request):
    return HttpResponse("<p>¡Funciona desde la View! HTMX + Django</p>")
########   Fin de código HTMX    #################
