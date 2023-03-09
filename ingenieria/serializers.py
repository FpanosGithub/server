from dataclasses import fields
from rest_framework import serializers
from ingenieria.models import TipoVehiculo, TipoEAVM, VersionCambiador
from ingenieria.models import TipoSistema, TipoConjunto, TipoComponente

class TipoComponenteSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = TipoComponente

class TipoConjuntoSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = TipoConjunto

class TipoSistemaSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = TipoSistema

class TipoVehiculoSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = TipoVehiculo

class TipoVehiculoMinimoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoVehiculo
        fields = ['id', 'codigo', 'descripcion']

class TipoEAVMSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = TipoEAVM

class TipoEAVMMinimoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoEAVM
        fields = ['id', 'codigo']

class VersionCambiadorSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = VersionCambiador

class VersionCambiadorMinimoSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ['id', 'codigo']
        model = VersionCambiador