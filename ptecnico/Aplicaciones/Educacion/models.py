from django.db import models

# Create your models here.
class Carrera(models.Model):
    id_car=models.AutoField(primary_key=True)
    nombre_car=models.CharField(max_length=250)
    fechacreacion_car=models.DateField()
    telefono_car=models.CharField(max_length=20)
    logo_car=models.FileField(upload_to='carreras',null=True)

    def __str__(self):
        return self.nombre_car   ## Se manda esta informac para que se muestre en el Panel-Admin de DJango


class Curso(models.Model):
    id_cur=models.AutoField(primary_key=True)
    nivel_cur=models.CharField(max_length=50)
    aula_cur=models.IntegerField()
    fk_id_car=models.ForeignKey(Carrera, on_delete=models.PROTECT)
    
    def __str__(self):
        return self.nivel_cur   ## Se manda esta informac para que se muestre en el Panel-Admin de DJango


class Materia(models.Model):
    id_mat=models.AutoField(primary_key=True)
    nombre_mat=models.CharField(max_length=60)
    creditos_mat=models.IntegerField()
    fk_id_cur=models.ForeignKey(Curso,on_delete=models.PROTECT)



