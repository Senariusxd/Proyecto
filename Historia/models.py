from django.db import models


class Enfermedad(models.Model):
    nombre = models.CharField(max_length=50)
    
    def __str__(self):
        return self.nombre

class Grupos(models.Model):
    nombre = models.CharField(max_length=50, primary_key=True)
    
    def __str__(self):
        return self.nombre
    
class Historial(models.Model):
    id = models.CharField(max_length=50, primary_key=True)
    fecha = models.CharField(max_length=50)
    paciente = models.ForeignKey('Paciente', on_delete=models.CASCADE, related_name='historial', null=True)
    ExamenMedico = models.CharField(max_length=50)
    ExamenFisico = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre
    
class Paciente(models.Model):
    nombre = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    ci = models.CharField(max_length=50, primary_key=True)
    telefono = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50)
    ocupacion = models.CharField(max_length=50)
    grupos = models.ForeignKey(Grupos, on_delete=models.CASCADE, related_name='pacientes')

    def __str__(self):
        return self.nombre
    
class EF(models.Model):
    paciente = models.ForeignKey('Paciente', on_delete=models.CASCADE, related_name='ef', null=True)
    pielymucosa = models.CharField(max_length=50)
    tcs = models.CharField(max_length=50)
    mamas = models.CharField(max_length=50)
    acv = models.CharField(max_length=50)
    abdomen = models.CharField(max_length=50)
    snc = models.CharField(max_length=50)
    soma = models.CharField(max_length=50)
    genitalesexternos = models.CharField(max_length=50)
    conducta = models.CharField(max_length=50)

class EM(models.Model):
    paciente = models.ForeignKey('Paciente', on_delete=models.CASCADE, related_name='em', null=True)
    edad = models.CharField(max_length=50)
    sexi = models.CharField(max_length=50)
    appersonales = models.CharField(max_length=50)
    apfamiliares = models.CharField(max_length=50)
    vicio = models.CharField(max_length=50)
    enfermedad = models.ForeignKey(Enfermedad, on_delete=models.CASCADE, related_name='historial', null=True)
    opreciones = models.CharField(max_length=50)
    transfuciones = models.CharField(max_length=50)
    vacunacion = models.CharField(max_length=50)
    alergico = models.CharField(max_length=50)
