from django.shortcuts import render,HttpResponse, redirect
from Aplicaciones.Educacion.models import Curso, Carrera 
from django.contrib import messages

def cursos(request):
    cursosDbb=Curso.objects.all()
    carrerasDbb=Carrera.objects.all()
    return render(request,'cursos.html', 
                  {"cursos":cursosDbb, "carreras":carrerasDbb})


def crear_curso(request):
    if request.method=='POST':
        nivel=request.POST['nivel_cur']
        aula=request.POST['aula_cur']
        fk_id_car=request.POST['fk_id_car']

        carrera_select=Carrera.objects.get(id_car=fk_id_car)
        ## Comando ORM (object Relational Mapping) para hacer el insert en la tabla
        Curso.objects.create(nivel_cur=nivel, aula_cur=aula, fk_id_car=carrera_select)

        messages.success(request, "Curso creada correctamente.")
        ## Hacer return redirect para actualizar tabla html de cursos
        cursosDbb=Curso.objects.all()
        carrerasDbb=Carrera.objects.all()
        return render(request,'cursos.html',{"cursos":cursosDbb, "carreras":carrerasDbb})


def eliminar_curso(request, id):
    cursoDB=Curso.objects.get(id_cur=id)
    cursoDB.delete()
    messages.success(request,"Curso borrada correctamente.")
    return redirect('/cursos')


def curso_editar(request, id):
    cursoDB=Curso.objects.get(id_cur=id)
    carrerasDB=Carrera.objects.all()
    return render(request, 'curso_editar.html', {"curso":cursoDB, "carreras":carrerasDB})



def procesar_editar_curso(request): 
    if request.method=='POST':
        curso=request.POST['id_cur']
        nivel=request.POST['nivel_cur']
        aula=request.POST['aula_cur']
        fk_id_car=request.POST['fk_id_car']

        carrera_select=Carrera.objects.get(id_car=fk_id_car)
        ## Comando ORM (object Relational Mapping) para hacer el UPDATE en la tabla
        curso_editar=Curso.objects.get(id_cur=curso)
        curso_editar.nivel_cur=nivel
        curso_editar.aula_cur=aula
        curso_editar.fk_id_car=carrera_select
        curso_editar.save()

        messages.success(request, "Curso actualizado correctamente.")
        ## Hacer return redirect para actualizar tabla html de cursos
        return redirect('/cursos')


       