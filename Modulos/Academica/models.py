from django.db import models

# Create your models here.
class Carrera(models.Model):
    codigo = models.CharField(max_length=3, primary_key=True)
    nombre = models.CharField(max_length=50)
    duracion = models.PositiveSmallIntegerField(default=5)

    def __str__(self):
        return f"{self.nombre} Duracion:{self.duracion} Años"

class Estudiante(models.Model):
    dni = models.CharField(max_length=8, primary_key=True)
    apellido_paterno = models.CharField(max_length=35)
    apellido_materno = models.CharField(max_length=35)
    nombre = models.CharField(max_length=35)
    fecha_nacimiento = models.DateField()
    sexos = {
        ('F','Femenino'),
        ('M','Masculino')
    }
    sexo = models.CharField(max_length=1,choices=sexos, default='M')
    carrera = models.ForeignKey(Carrera, null=False, blank=False, on_delete=models.CASCADE)
    vigencia = models.BooleanField(default=True)

    def nombre_completo(self):
        return f"{self.apellido_paterno} {self.apellido_materno}, {self.nombre}"

    def __str__(self):
        if self.vigencia:
            estado_estudiante = 'VIGENTE'
        else:
            estado_estudiante = 'DE BAJA'
        return f"{self.nombre_completo()} / {self.carrera}/ {estado_estudiante}"

class Curso(models.Model):
    codigo = models.CharField(max_length=6, primary_key=True)
    nombre = models.CharField(max_length=30)
    creditos = models.PositiveSmallIntegerField()
    docente = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nombre} {self.codigo} Diocente: {self.docente}"

class Matricula(models.Model):
    id = models.AutoField(primary_key=True)
    estudiante = models.ForeignKey(Estudiante, null=False, blank=False, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, null=False, blank=False, on_delete=models.CASCADE)
    fecha_matricula = models.DateTimeField(auto_created=True)

    def __str__(self):
        if self.estudiante.sexo == 'F':
            letra_sexo = 'a'
        else:
            letra_sexo = 'o'
        
        fecha_mat = self.fecha_matricula.strftime("%A %d/%m/%Y %H:%M:%S")

        return f"{self.estudiante.nombre_completo()} matricula{letra_sexo} en el curso {self.curso} / Fecha: {fecha_mat}"
