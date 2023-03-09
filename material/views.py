from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes

# Importaciones de distintas apps
# material
from material.models import EAVM, Vehiculo
from material.serializers import EAVMSerializer, VehiculoSerializer

#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# EJES
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# material/EAVMs
@api_view(['GET'])
@permission_classes([AllowAny])
def SeleccionEAVMs(request):
    EAVMs = EAVM.objects.all().order_by('-id')
    #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    serializer = EAVMSerializer(EAVMs, many= True)
    return Response(serializer.data)

# material/EAVM/1/
@api_view(['GET'])
@permission_classes([AllowAny])
def DetalleEAVM(request, id=1):
    EAVM = EAVM.objects.get(id=id)
    #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    serializer = EAVMSerializer(EAVM, many= False)
    return Response(serializer.data)

# material/EAVMs920
@api_view(['GET'])
@permission_classes([AllowAny])
def Seleccion920(request):
    EAVMs = EAVM.objects.filter(tipo_EAVM__codigo__contains='920')
    #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    serializer = EAVMSerializer(EAVMs, many= True)
    return Response(serializer.data)

# vehiculos/ejes760
@api_view(['GET'])
@permission_classes([AllowAny])
def Seleccion760(request):
    EAVMs = EAVM.objects.filter(tipo_EAVM__codigo__contains='760')
    #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    serializer = EAVMSerializer(EAVMs, many= True)
    return Response(serializer.data)

#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# VEHÍCULOS
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# material/vehiculos
@api_view(['GET'])
@permission_classes([AllowAny])
def SeleccionVehiculos(request):
    vehiculos = Vehiculo.objects.all().order_by('-id')
    #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    serializer = VehiculoSerializer(vehiculos, many= True)
    return Response(serializer.data)

# material/vehiculos/1/
@api_view(['GET'])
@permission_classes([AllowAny])
def DetalleVehiculo(request, id=1):
    vehiculo = Vehiculo.objects.get(id=id)
    #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    serializer = VehiculoSerializer(vehiculo, many= False)
    return Response(serializer.data)

# material/vehiculos/locomotoras
@api_view(['GET'])
@permission_classes([AllowAny])
def SeleccionLocomotoras(request):
    vehiculos = Vehiculo.objects.filter(tipo__clase = 'LOC').order_by('-id')
    #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    serializer = VehiculoSerializer(vehiculos, many= True)
    return Response(serializer.data)

# material/vehiculos/auxiliares
@api_view(['GET'])
@permission_classes([AllowAny])
def SeleccionAuxiliares(request):
    vehiculos = Vehiculo.objects.filter(tipo__clase = 'MRA').order_by('-id')
    #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    serializer = VehiculoSerializer(vehiculos, many= True)
    return Response(serializer.data)

# material/vehiculos/vagones
@api_view(['GET'])
@permission_classes([AllowAny])
def SeleccionVagones(request):
    vehiculos = Vehiculo.objects.filter(tipo__clase = 'VAG').order_by('-id')
    #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    serializer = VehiculoSerializer(vehiculos, many= True)
    return Response(serializer.data)