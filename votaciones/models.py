from django.db import models


# Create your models here.

TIPO_EVENTO =  (
            ('G','Generales'),
            ('A','Autonomicas'),
            ('L','Locales'),
            )


class Usuario (models.Model):
    dni= models.CharField(unique = True, max_length=9 )
    nombre= models.CharField(max_length = 30)
    apellido1 = models.CharField(max_length = 30)
    apellido2 = models.CharField(max_length = 30)
    fecha_nac = models.DateField()
    municipio = models.CharField(max_length = 30)
    domicilio = models.CharField(max_length = 50)
    email = models.EmailField()
    telefono = models.CharField(max_length = 12)
    mesa = models.PositiveIntegerField(default=0)

    def __str__(self):
        return '%s %s %s %s' % (self.dni, self.nombre, self.apellido1, self.apellido2)
    class Meta:
        ordering = ('dni',)

class Evento (models.Model):
    nombre = models.CharField(max_length = 100)
    votantes= models.ManyToManyField(Usuario,blank = True, default = None)
    fecha = models.DateField('Fecha evento')
    categoria = models.CharField (choices = TIPO_EVENTO, max_length = 1)
    # num_votantes_total = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.nombre

    # def get_percentage(self):
    #     perc = self.votantes.count() * 100 / self.num_votantes_total
    #     return perc

    class Meta:
        ordering = ('nombre',)



