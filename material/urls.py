from django.urls import path

# Ejes
from material.views import SeleccionEAVMs, DetalleEAVM, Seleccion920, Seleccion760
# Vehiculos
from material.views import SeleccionVehiculos, DetalleVehiculo, SeleccionLocomotoras, SeleccionAuxiliares, SeleccionVagones

urlpatterns = [
    # EJES
    path('EAVMs', SeleccionEAVMs, name = 'EAVMs'),
    path('EAVMs/<int:id>/', DetalleEAVM, name = 'detalle_EAVM'),
    path('EAVMs920', Seleccion920, name = 'EAVMs920'),
    path('EAVMs760', Seleccion760, name = 'EAVMs760'),
    # VEHÍCULOS 
    path('vehiculos', SeleccionVehiculos, name = 'vehiculos'),
    path('vehiculos/<int:id>/', DetalleVehiculo, name = 'detalle_vehiculo'),
    path('vehiculos/locomotoras', SeleccionLocomotoras, name = 'locomotoras'),
    path('vehiculos/auxiliares', SeleccionAuxiliares, name = 'auxiliares'),
    path('vehiculos/vagones', SeleccionVagones, name = 'vagones'),
]