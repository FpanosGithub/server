from rest_framework import serializers
from material.models import Vehiculo, ComponenteVehiculo, ConjuntoVehiculo, SistemaVehiculo
from material.models import EAVM, ComponenteEAVM, ConjuntoEAVM, SistemaEAVM
from ingenieria.serializers import TipoVehiculoSerializer, TipoSistemaSerializer, TipoConjuntoSerializer, TipoComponenteSerializer

#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# SERIALIZACIÓN DE EAVM
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
class ComponentesConjuntoEAVMSerializer(serializers.ModelSerializer):
    componente = TipoComponenteSerializer(many=False, read_only=True)
    class Meta:
        fields = '__all__'
        model = ComponenteEAVM

class ConjuntosSistemaEAVMSerializer(serializers.ModelSerializer):
    conjunto = TipoConjuntoSerializer(many=False, read_only=True)
    componentes = ComponentesConjuntoEAVMSerializer(many=True, read_only=True)
    class Meta:
        fields = '__all__'
        model = ConjuntoEAVM

class SistemasVehiculoSerializer(serializers.ModelSerializer):
    sistema = TipoSistemaSerializer(many=False, read_only=True)
    conjuntos = ConjuntosSistemaEAVMSerializer(many=True, read_only=True)
    class Meta:
        fields = '__all__'
        model = SistemaEAVM

class EAVMMinimoSerializer(serializers.ModelSerializer):
    class Meta:
        model = EAVM
        fields = ['id', 'codigo']

class VehiculoMinimoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehiculo
        fields = ['id', 'matricula']

class EAVMSerializer(serializers.ModelSerializer):
    tipo_EAVM = serializers.StringRelatedField(many=False)
    fabricante = serializers.StringRelatedField(many=False)
    keeper = serializers.StringRelatedField(many=False)
    owner = serializers.StringRelatedField(many=False)
    EEM = serializers.StringRelatedField(many=False)
    bogie = serializers.StringRelatedField(many=False)
    vehiculo = VehiculoMinimoSerializer(many=False, read_only=True)
    class Meta:
        fields = '__all__'
        model = EAVM

#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# SERIALIZACIÓN DE VEHÍCULOS
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
class ComponentesConjuntoVehiculoSerializer(serializers.ModelSerializer):
    componente = TipoComponenteSerializer(many=False, read_only=True)
    class Meta:
        fields = '__all__'
        model = ComponenteVehiculo

class ConjuntosSistemaVehiculoSerializer(serializers.ModelSerializer):
    conjunto = TipoConjuntoSerializer(many=False, read_only=True)
    componentes = ComponentesConjuntoVehiculoSerializer(many=True, read_only=True)
    class Meta:
        fields = '__all__'
        model = ConjuntoVehiculo

class SistemasVehiculoSerializer(serializers.ModelSerializer):
    sistema = TipoSistemaSerializer(many=False, read_only=True)
    conjuntos = ConjuntosSistemaVehiculoSerializer(many=True, read_only=True)
    class Meta:
        fields = '__all__'
        model = SistemaVehiculo

class VehiculoSerializer(serializers.ModelSerializer):
    tipo = TipoVehiculoSerializer(many=False, read_only=True)
    fabricante = serializers.StringRelatedField(many=False)
    keeper = serializers.StringRelatedField(many=False)
    owner = serializers.StringRelatedField(many=False)
    EEM = serializers.StringRelatedField(many=False)
    ejes = EAVMMinimoSerializer(many=True, read_only=True)
    sistemas = SistemasVehiculoSerializer(many=True, read_only=True)
    class Meta:
        fields = '__all__'
        model = Vehiculo