from django.db import models
from django.urls import reverse
from organizaciones.models import Owner, Fabricante, EEM, Keeper
from ingenieria.models import TipoVehiculo, TipoEAVM, TipoSistema, TipoConjunto, TipoComponente

#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# 1. VEHICULOS
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

class Vehiculo(models.Model):
    # Descripción del vehiculo
    tipo = models.ForeignKey(TipoVehiculo, on_delete=models.CASCADE, null=True, blank=True)
    num_uic = models.CharField(max_length=17, unique= True, default = '', null=True, blank=True)
    descripcion_particular = models.CharField(max_length=50, default = '', null=True, blank=True)
    #!!!!!!!!
    km_origen = models.FloatField(default=0)                  # km que llevaba cuando la EEM lo asumió
    fecha_origen = models.DateField(default = "2022-01-01")   # cuando lo asumión la EEM
    #!!!!!!!!
    # Quien es quién
    owner= models.ForeignKey(Owner, on_delete=models.RESTRICT, null=True, blank=True)
    keeper= models.ForeignKey(Keeper, on_delete=models.RESTRICT, null=True, blank=True)
    fabricante= models.ForeignKey(Fabricante, on_delete=models.RESTRICT, null=True, blank=True)
    EEM= models.ForeignKey(EEM, on_delete=models.RESTRICT, null=True, blank=True)
    fecha_fab = models.DateField(null=True, blank=True)
    # Mantenimiento del Vehículo
    fecha_ultimo_mantenimiento = models.DateField(null=True, blank=True)    # cuando terminó el último mantenimiento
    fecha_proximo_mantenimiento = models.DateField(null=True, blank=True)    # cuando será el proximo mantenimiento
    km_ultimo_mant = models.FloatField(default=0, null=True, blank=True)
    km_proximo_mant = models.FloatField(default=0, null=True, blank=True)
    nivel_proximo_mant = models.IntegerField(default=0)
    # Variables estado vehículo
    en_servicio = models.BooleanField(default=True)
    en_mantenimiento = models.BooleanField(default=True)
    en_circulacion = models.BooleanField(default=True)
    en_nudo = models.BooleanField(default=False)
    transmitiendo = models.BooleanField(default=False)
    alarma_circulacion = models.BooleanField(default=False)
    alarma_mantenimiento = models.BooleanField(default=False)
    ultimo_evento_dt = models.DateTimeField(null=True, blank=True)
    observaciones_servicio = models.CharField(max_length=80, default = 'sin observaciones')
    vel = models.FloatField(default=0, null=True, blank=True)
    lng = models.FloatField(default=-3.9820) # grados
    lat = models.FloatField(default=40.2951) # grados
    #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    km_totales = models.FloatField(default=0)           # km origen + km circulados
    #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    def __str__(self):
        return self.num_uic

class SistemaVehiculo(models.Model):
    sistema = models.ForeignKey(TipoSistema, on_delete=models.RESTRICT, null=True, blank=True)
    vehiculo= models.ForeignKey(Vehiculo, on_delete=models.RESTRICT, null=True, blank=True)
    descripcion_particular = models.CharField(max_length=20, default = '', null=True, blank=True)
    def __str__(self):
        return self.sistema.codigo

class ConjuntoVehiculo(models.Model):
    conjunto = models.ForeignKey(TipoConjunto, on_delete=models.RESTRICT, null=True, blank=True)
    sistema= models.ForeignKey(SistemaVehiculo, on_delete=models.RESTRICT, null=True, blank=True)
    descripcion_particular = models.CharField(max_length=20, default = '', null=True, blank=True)
    num_unidades = models.IntegerField(default=0)
    def __str__(self):
        return self.conjunto.codigo

class ComponenteVehiculo(models.Model):
    componente = models.ForeignKey(TipoComponente, on_delete=models.RESTRICT, null=True, blank=True)
    conjunto = models.ForeignKey(ConjuntoVehiculo, on_delete=models.CASCADE, null=True, blank=True)
    num_unidades = models.IntegerField(default=0)
    def __str__(self):
        return self.componente.codigo
    
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# 2 EJES EAVM MONTADO
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

class EAVM(models.Model):
    #Identificación
    codigo = models.CharField(max_length=16, unique= True)
    tipo_EAVM = models.ForeignKey(TipoEAVM, on_delete=models.RESTRICT, null=True, blank=True)
    num_uic = models.CharField(max_length=17, unique= True, default = '', null=True, blank=True)
    #!!!!!!!!
    km_origen = models.FloatField(default=0)                    # km que llevaba cuando la EEM lo asumió
    fecha_origen = models.DateField(default = "2022-01-01")     # cuando lo asumión la EEM
    #!!!!!!!!
    #Quien es quién
    owner = models.ForeignKey(Owner, on_delete=models.RESTRICT, null=True, blank=True)
    fabricante = models.ForeignKey(Fabricante, on_delete=models.RESTRICT, limit_choices_to={'de_ejes': True},null=True, blank=True)
    fecha_fab = models.DateField(null=True, blank=True)
    keeper = models.ForeignKey(Keeper, on_delete=models.RESTRICT, null=True, blank=True)
    EEM = models.ForeignKey(EEM, on_delete=models.RESTRICT, null=True, blank=True)
    # Situación de Mantenimiento
    fecha_ultimo_mantenimiento = models.DateField(null=True, blank=True) 
    fecha_proximo_mantenimiento = models.DateField(null=True, blank=True)    # cuando será el proximo mantenimiento
    km_proximo_mant = models.FloatField(default=0)
    nivel_proximo_mant = models.IntegerField(default=0)
    # Vehículo donde va el eje
    vehiculo = models.ForeignKey(Vehiculo, related_name='ejes', on_delete=models.RESTRICT, null=True, blank=True)
    # Variables estado eje
    en_servicio = models.BooleanField(default=True)
    en_mantenimiento = models.BooleanField(default=True)
    en_circulacion = models.BooleanField(default=True)
    observaciones_servicio = models.CharField(max_length=80, default = 'sin observaciones')
    alarma_temp = models.BooleanField(default=False)
    alarma_aceleraciones = models.BooleanField(default=False)
    alarma_cambio = models.BooleanField(null=True,default=False)
    alarma_mantenimiento = models.BooleanField(null=True,default=False)
    tempa = models.FloatField(default=25.0, null=True, blank=True)
    tempb = models.FloatField(default=25.0, null=True, blank=True)
    lng = models.FloatField(default=-3.9820)
    lat = models.FloatField(default=40.2951)
    #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    #Vida del eje
    num_cambios = models.IntegerField(default=0)
    km_totales = models.FloatField(default=0)           # km origen + km circulados
    coef_trabajo = models.FloatField(default=0)
    #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    def __str__(self):
        return self.codigo

class SistemaEAVM(models.Model):
    sistema = models.ForeignKey(TipoSistema, on_delete=models.RESTRICT, null=True, blank=True)
    EAVM = models.ForeignKey(EAVM, on_delete=models.RESTRICT, null=True, blank=True)
    descripcion_particular = models.CharField(max_length=20, default = '', null=True, blank=True)
    def __str__(self):
        return self.sistema.codigo

class ConjuntoEAVM(models.Model):
    conjunto = models.ForeignKey(TipoConjunto, on_delete=models.RESTRICT, null=True, blank=True)
    sistema = models.ForeignKey(SistemaEAVM, on_delete=models.RESTRICT, null=True, blank=True)
    descripcion_particular = models.CharField(max_length=20, default = '', null=True, blank=True)
    num_unidades = models.IntegerField(default=0)
    def __str__(self):
        return self.conjunto.codigo

class ComponenteEAVM(models.Model):
    componente = models.ForeignKey(TipoComponente, on_delete=models.RESTRICT, null=True, blank=True)
    conjunto = models.ForeignKey(ConjuntoEAVM, on_delete=models.CASCADE, null=True, blank=True)
    num_unidades = models.IntegerField(default=0)
    def __str__(self):
        return self.componente.codigo