from django.urls import path
# Generales
# Vehiculos
from eventos.views import CirculacionesVehiculo, EventosCirculacionVehiculo, CirculacionesVehiculoAmpliadas
from eventos.views import CirculacionesEAVM, EventosCirculacionEAVM, CirculacionesEAVMAmpliadas, CambiosEAVM

urlpatterns = [
    # VEHÍCULOS 
    path('circulaciones_vehiculo/<int:id>/', CirculacionesVehiculo, name = 'circulaciones_vehiculo'),
    path('eventos_circulacion_vehiculo/<int:id>/', EventosCirculacionVehiculo, name = 'eventos_circulacion_vehiculo'),
    path('circulaciones_vehiculo_ampliadas/<int:id>/', CirculacionesVehiculoAmpliadas, name = 'circulaciones_vehiculo_ampliadas'),
    # EJES 
    path('circulaciones_EAVM/<int:id>/', CirculacionesEAVM, name = 'circulaciones_EAVM'),
    path('eventos_circulacion_EAVM/<int:id>/', EventosCirculacionEAVM, name = 'eventos_circulacion_EAVM'),
    path('circulaciones_EAVM_ampliadas/<int:id>/', CirculacionesEAVMAmpliadas, name = 'circulaciones_EAVM_ampliadas'),
    path('cambios_EAVM/<int:id>/', CambiosEAVM, name = 'cambios_EAVM'),
]