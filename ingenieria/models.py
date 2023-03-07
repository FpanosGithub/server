from django.db import models
from django.urls import reverse
from organizaciones.models import Fabricante, Diseñador, Aprovador, Certificador
from mantenimiento.models import PlanMantenimiento

#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# Modelos que representan la descripción técnica de todos los elementos del material rodante
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# 1. VEHÍCULOS, sus sistemas, conjuntos y elementos
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
class TipoVehiculo(models.Model):
    opciones_clase =    [   ('LOC', 'Locomotora de línea'),
                            ('VAG', 'Vagón de mercancías remolcado'),
                            ('MRA', 'Material Rodante Auxiliar'),
                        ]
    clase= models.CharField(max_length=16, choices = opciones_clase, default = 'MRA')
    descripcion = models.CharField(max_length=50, unique= True)
    marca = models.CharField(max_length=50, unique= True)
    modelo = models.CharField(max_length=50, unique= True)
    tipo_uic = models.CharField(max_length=4)
    serie_uic = models.CharField(max_length=4)
    num_bogies = models.IntegerField(default=0, null=True, blank=True)
    imagen = models.CharField(max_length=30,default = ' ', null=True, blank=True)
    slug_doc_tec = models.CharField(max_length=30, default = ' ', null=True, blank=True)
    #pm = models.ForeignKey(PlanMantenimiento, on_delete=models.RESTRICT, null=True, blank=True)
    def __str__(self):
        return self.codigo
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# 1.1 Sistemas en los vehículos (todo menos ejes y distribuidores)
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
class Sistema(models.Model):
    codigo= models.CharField(max_length=16, unique= True, null=True, blank=True)
    descripcion = models.CharField(max_length=50, null=True, blank=True)
    slug_doc = models.CharField(max_length=30, default = ' ', null=True, blank=True)
    def __str__(self):
        return self.codigo

class Componente(models.Model):
    sistema = models.ForeignKey(Sistema, on_delete=models.CASCADE, null=True, blank=True)
    codigo= models.CharField(max_length=16, unique= True, null=True, blank=True)
    descripcion = models.CharField(max_length=50, null=True, blank=True)
    slug_doc = models.CharField(max_length=30, default = ' ', null=True, blank=True)
    def __str__(self):
        return self.codigo

class ITM(models.Model):
    componente = models.ForeignKey(Componente, on_delete=models.CASCADE)
    codigo = models.CharField(max_length=16, unique= True)
    definicion = models.CharField(max_length=50, unique= True)
    n1 = models.BooleanField(default=True)
    n2 = models.BooleanField(default=True)
    n3 = models.BooleanField(default=True)
    n4 = models.BooleanField(default=True)
    n5 = models.BooleanField(default=True)
    descripcion = models.CharField(max_length=300, unique= True)
    valor_min = models.FloatField(null=True, blank=True)
    valor_max = models.FloatField(null=True, blank=True)
    unidades_medida = models.CharField(max_length=6, null=True, blank=True)
    slug_doc = models.CharField(max_length=30, default = ' ', null=True, blank=True)
    def __str__(self):
        return self.codigo

#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# 1.2 Ejes
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
class TipoEje(models.Model):
    codigo= models.CharField(max_length=16, unique= True)
    opciones_anchos =  [('UIC-IB', 'UIC(1435) <> IBÉRICO (1668)'),
                        ('UIC-RUS', 'UIC(1435) <> RUSO (1520)'),
                        ('UIC-RUS-IB', 'UIC <> RUSO <> IBÉRICO'),
                        ('METR-UIC', 'MÉTRICO(1000) <> UIC(1435)'),
                        ('UIC', 'UIC (1435)'),
                        ('IB', 'IB (1668)')]
    anchos = models.CharField(max_length=12, choices = opciones_anchos, default = 'UIC-IB')
    diseñador = models.ForeignKey(Diseñador, on_delete=models.RESTRICT, limit_choices_to={'de_ejes': True},)
    aprovador = models.ForeignKey(Aprovador, on_delete=models.RESTRICT)
    fecha_aprovacion = models.DateField(null=True, blank=True)
    certificador = models.ForeignKey(Certificador, on_delete=models.RESTRICT)
    fecha_certificacion = models.DateField(null=True, blank=True)
    documentacion_tecnica = models.CharField(max_length=30, default = ' ', null=True, blank=True)
    plan_mantenimiento = models.ForeignKey(PlanMantenimiento, on_delete=models.RESTRICT, null=True, blank=True)
    imagen = models.CharField(max_length=30,default = ' ', null=True, blank=True)
    def __str__(self):
        return self.codigo

class TipoConjuntoEje(models.Model):
    tipo_eje = models.ForeignKey(TipoEje, on_delete=models.CASCADE)
    codigo= models.CharField(max_length=16, unique= True)
    descripción = models.CharField(max_length=50, unique= True)
    documentacion_tecnica = models.CharField(max_length=30, default = ' ', null=True, blank=True)
    def __str__(self):
        return (str(self.tipo_eje.codigo) + '-' + str(self.codigo))

class TipoElementoEje(models.Model):
    tipo_conjunto = models.ForeignKey(TipoConjuntoEje, on_delete=models.CASCADE)
    codigo= models.CharField(max_length=16, unique= True)
    descripción = models.CharField(max_length=50, unique= True)
    documentacion_tecnica = models.CharField(max_length=30, default = ' ', null=True, blank=True)
    def __str__(self):
        return (str(self.tipo_conjunto.tipo_eje.codigo) + '-' + str(self.tipo_conjunto.codigo) + '-' + str(self.codigo))

class ConsistenciaEje(models.Model):
    tipo_conjunto = models.ForeignKey(TipoConjuntoEje, on_delete=models.CASCADE)
    codigo= models.CharField(max_length=16, unique= True)
    nivel_entrada = models.IntegerField(default = 1)
    descripción = models.CharField(max_length=300, unique= True)
    valor_min = models.FloatField(null=True, blank=True)
    valor_max = models.FloatField(null=True, blank=True)
    unidades_medida = models.CharField(max_length=6, null=True, blank=True)
    instruccion_tecnica = models.CharField(max_length=30, default = ' ', null=True, blank=True)
    def __str__(self):
        return (str(self.tipo_conjunto.tipo_eje.codigo) + '-' + str(self.tipo_conjunto.codigo) + '-' + str(self.codigo))


#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# Morfología de un tipo de vehículo
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
class SistemasVehiculo(models.Model):
    vehiculo = models.ForeignKey(TipoVehiculo, on_delete=models.CASCADE, null=True, blank=True)
    sistema = models.ForeignKey(Sistema, on_delete=models.CASCADE, null=True, blank=True)

class EjesVehiculo(models.Model):
    vehiculo = models.ForeignKey(TipoVehiculo, on_delete=models.CASCADE, null=True, blank=True)
    eje = models.ForeignKey(TipoEje, on_delete=models.CASCADE, null=True, blank=True)
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!


#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# 1. CAMBIADORES
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
class VersionCambiador(models.Model):
    codigo= models.CharField(max_length=16, unique= True)
    opciones_anchos =  [('UIC-IB', 'UIC(1435) <> IBÉRICO (1668)'),
                        ('UIC-RUS', 'UIC(1435) <> RUSO (1520)'),
                        ('METR-UIC', 'MÉTRICO(1000) <> UIC(1435)'),
                        ]
    anchos = models.CharField(max_length=12, choices = opciones_anchos, default = 'UIC-IB')
    diseñador = models.ForeignKey(Diseñador, on_delete=models.RESTRICT, limit_choices_to={'de_cambiadores': True},)
    fabricante = models.ForeignKey(Fabricante, on_delete=models.RESTRICT, limit_choices_to={'de_cambiadores': True}, null=True, blank=True)
    longitud_desencerrojado = models.FloatField(default=6000)   # mm
    longitud_cambio_rueda = models.FloatField(default=6000)     # mm
    longitud_encerrojado = models.FloatField(default=6000)      # mm
    longitud_total = models.FloatField(default = 36000)         # mm
    aprovador = models.ForeignKey(Aprovador, on_delete=models.RESTRICT)
    fecha_aprovacion = models.DateField(null=True, blank=True)
    certificador = models.ForeignKey(Certificador, on_delete=models.RESTRICT)
    fecha_certificacion = models.DateField(null=True, blank=True)
    def __str__(self):
        return self.codigo
    def get_absolute_url(self):
        return reverse("ficha_version_cambiador", kwargs={'pk':self.pk})


