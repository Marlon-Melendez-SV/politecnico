# Generated by Django 5.2.2 on 2025-06-10 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Educacion', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='carrera',
            name='logo_car',
            field=models.FileField(null=True, upload_to='carreras'),
        ),
        migrations.AlterField(
            model_name='carrera',
            name='nombre_car',
            field=models.CharField(max_length=250),
        ),
    ]
