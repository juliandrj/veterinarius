from django.db import models
from django.contrib.auth.models import User, Group

class Persona(models.Model):
    nuid = models.CharField(max_length=64, unique=True, blank=False, null=False)
    direccion = models.CharField(max_length=128, blank=False, null=False)
    telefono = models.CharField(max_length=128, blank=False, null=False)
    usuario = models.ForeignKey(User, on_delete=models.PROTECT)
    def __str__(self):
        return self.usuario.first_name + ' (' + self.nuid + ')'
    class Meta:
        ordering = ('nuid',)

class Especie(models.Model):
    especie = models.CharField(max_length=128, blank=False, null=False)
    def __str__(self):
        return self.especie
    class Meta:
        ordering = ('especie',)

class Raza(models.Model):
    especie = models.ForeignKey(Especie, on_delete=models.PROTECT)
    raza = models.CharField(max_length=128, blank=False, null=False)
    def __str__(self):
        return self.raza
    class Meta:
        ordering = ('raza',)

class Genero(models.Model):
    genero = models.CharField(max_length=128, blank=False, null=False)
    def __str__(self):
        return self.genero
    class Meta:
        ordering = ('genero',)

class Propietario(Persona):
    def __str__(self):
        return '[prop]' + self.usuario.first_name
    class Meta:
        ordering = ('pk',)

class Medico(Persona):
    tarjeta_profesional = models.CharField(max_length=64, unique=True, blank=False, null=False)
    ruta_firma = models.CharField(max_length=512, blank=False, null=False)
    def __str__(self):
        return '[vet]' + self.usuario.first_name
    class Meta:
        ordering = ('tarjeta_profesional',)

class Mascota(models.Model):
    nombre = models.CharField(max_length=256, blank=False, null=False)
    fecha_nacimiento = models.DateField(null=False)
    ruta_foto = models.CharField(max_length=512, blank=False, null=False)
    genero = models.ForeignKey(Genero, on_delete=models.PROTECT)
    raza = models.ForeignKey(Raza, on_delete=models.PROTECT)
    propietario = models.ForeignKey(Propietario, on_delete=models.PROTECT)
    def __str__(self):
        return '[' + self.raza.raza + '] ' + self.nombre
    class Meta:
        ordering = ('nombre',)

class Agenda(models.Model):
    medico = models.ForeignKey(Medico, on_delete=models.PROTECT)
    mascota = models.ForeignKey(Mascota, on_delete=models.PROTECT)
    fecha = models.DateTimeField(null=False)
    # def __str__(self):
    #     return self.fecha + ' - ' + self.medicov + ': ' + self.mascota
    class Meta:
        ordering = ('fecha',)

class OpcionMenu(models.Model):
    label = models.CharField(max_length=256, blank=False, null=False)
    ruta = models.CharField(max_length=256, blank=True, null=True)
    grupo = models.ForeignKey(Group, on_delete=models.PROTECT)
    opcion_padre = models.ForeignKey('self', on_delete=models.PROTECT, null=True, blank=True)
    def __str__(self):
        return '[' + self.grupo.name + '] ' + self.label
    class Meta:
        ordering = ('label',)
