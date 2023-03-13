from django.db import models
from django.urls import reverse
from organizaciones.models import Fabricante, Diseñador, Aprovador, Certificador

#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# Modelos que representan la descripción técnica de todos los elementos del material rodante
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# 0. PLANES DE MANTENIMIENTO DE VEHÍCULOS Y EJES
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
class PlanMantenimiento(models.Model):
    codigo = models.CharField(max_length=16, unique= True)
    descripcion = models.CharField(max_length=300, null=True, blank=True)
    num_niveles = models.IntegerField(default=3, null=True, blank=True)
    def __str__(self):
        return ('Slug: ' + str(self.pk) + ' // Código: ' + str(self.codigo))

class NivelesPlan(models.Model):
    pm = models.ForeignKey(PlanMantenimiento, on_delete=models.CASCADE, null=True, blank=True)
    num_nivel = models.IntegerField(default=0, null=True, blank=True)
    cod_nivel = models.CharField(max_length=4, default = '', null=True, blank=True)
    dias_siguiente = models.IntegerField(default=365)
    km_siguiente = models.IntegerField(default=100000)
    def __str__(self):
        return ('Slug: ' + str(self.pk) + ' // Plan:' + str(self.pm.codigo) + '- Nivel: ' + str(self.cod_nivel))
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# 1. TIPOS DE VEHÍCULOS
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
class TipoVehiculo(models.Model):
    opciones_clase =    [   ('LOC', 'Locomotora de línea'),
                            ('VAG', 'Vagón de mercancías remolcado'),
                            ('MRA', 'Material Rodante Auxiliar'),
                        ]
    clase= models.CharField(max_length=16, choices = opciones_clase, default = 'MRA')
    descripcion = models.CharField(max_length=50, null=True, blank=True)
    marca = models.CharField(max_length=50, null=True, blank=True)
    modelo = models.CharField(max_length=50, null=True, blank=True)
    tipo_uic = models.CharField(max_length=4, null=True, blank=True)
    serie_uic = models.CharField(max_length=4, null=True, blank=True)
    #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    num_bogies = models.IntegerField(default=0, null=True, blank=True)
    carga_maxima = models.FloatField(null=True, blank=True)
    tara = models.FloatField(null=True, blank=True)
    peso_x_eje = models.FloatField(null=True, blank=True)
    velocidad = models.FloatField(null=True, blank=True)
    longitud = models.FloatField(null=True, blank=True)
    #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    imagen = models.CharField(max_length=30,default = ' ', null=True, blank=True)
    pm = models.ForeignKey(PlanMantenimiento, on_delete=models.RESTRICT, null=True, blank=True)
    def __str__(self):
        return ('Slug: ' + str(self.pk) + ' // Clase:' + str(self.clase) + '- tipo:' + str(self.tipo_uic) + '- Serie:' + str(self.serie_uic))
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# 2. TIPOS DE EAVM - Ejes Ancho Variable de Mercancias
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
class TipoEAVM(models.Model):
    codigo= models.CharField(max_length=16, unique= True)
    opciones_anchos =  [('UIC-IB', 'UIC(1435) <> IBÉRICO (1668)'),
                        ('UIC-RUS', 'UIC(1435) <> RUSO (1520)'),
                        ('UIC-RUS-IB', 'UIC <> RUSO <> IBÉRICO'),
                        ('METR-UIC', 'MÉTRICO(1000) <> UIC(1435)'),
                        ('UIC', 'UIC (1435)'),
                        ('IB', 'IB (1668)')]
    anchos = models.CharField(max_length=12, choices = opciones_anchos, default = 'UIC-IB')
    diseñador = models.ForeignKey(Diseñador, on_delete=models.RESTRICT, limit_choices_to={'de_ejes': True},)
    aprovador = models.ForeignKey(Aprovador, on_delete=models.RESTRICT, null=True, blank=True)
    fecha_aprovacion = models.DateField(null=True, blank=True)
    certificador = models.ForeignKey(Certificador, on_delete=models.RESTRICT, null=True, blank=True)
    fecha_certificacion = models.DateField(null=True, blank=True)
    imagen = models.CharField(max_length=30,default = '', null=True, blank=True)
    pm = models.ForeignKey(PlanMantenimiento, on_delete=models.RESTRICT, null=True, blank=True)
    def __str__(self):
        return ('Slug: ' + str(self.pk) + ' // Código: ' + str(self.codigo))

#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# 3. Sistemas conjuntos y componentes en los vehículos o en los EAVM
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
class TipoSistema(models.Model):
    codigo= models.CharField(max_length=16, unique= True, null=True, blank=True)
    descripcion = models.CharField(max_length=50, null=True, blank=True)
    def __str__(self):
        return ('Slug: ' + str(self.pk) + ' // Sistema:' + str(self.codigo) + ': ' + str(self.descripcion))

class TipoConjunto(models.Model):
    codigo= models.CharField(max_length=16, unique= True, null=True, blank=True)
    descripcion = models.CharField(max_length=50, null=True, blank=True)
    sistema = models.ForeignKey(TipoSistema, on_delete=models.CASCADE, null=True, blank=True)
    def __str__(self):
        return ('Slug: ' + str(self.pk) + ' // Sistema:' + str(self.sistema.codigo) + '- Conjunto:' + str(self.codigo))

class TipoComponente(models.Model):
    codigo= models.CharField(max_length=16, unique= True, null=True, blank=True)
    descripcion = models.CharField(max_length=50, null=True, blank=True)
    conjunto = models.ForeignKey(TipoConjunto, on_delete=models.CASCADE, null=True, blank=True)
    def __str__(self):
        return ('Slug: ' + str(self.pk) + ' // Sistema:' + str(self.conjunto.sistema.codigo) + '- Conjunto:' + str(self.conjunto.codigo) + 'Componente' + str(self.codigo))

#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# 4. TOPOLOGÍA DE LOS TIPOS DE VEHÍCULOS y DE EAVM
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!   
class SistemasVehiculo(models.Model):
    vehiculo = models.ForeignKey(TipoVehiculo, on_delete=models.CASCADE, null=True, blank=True)
    sistema = models.ForeignKey(TipoSistema, on_delete=models.CASCADE, null=True, blank=True)

class SistemasEAVM(models.Model):
    EAVM = models.ForeignKey(TipoEAVM, on_delete=models.CASCADE, null=True, blank=True)
    sistema = models.ForeignKey(TipoSistema, on_delete=models.CASCADE, null=True, blank=True)

#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# 5. INSTRUCCIONES TECNICAS DE MANTENIMIENTO DE COMPONENTES
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
class InstruccionTecnica(models.Model):
    componente = models.ForeignKey(TipoComponente, on_delete=models.CASCADE)
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
    def __str__(self):
        return ('Slug: ' + str(self.pk) + ' // Componente: ' + str(self.componenente.codigo) + ' - IT: ' + str(self.codigo))

#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# CAMBIADORES
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


