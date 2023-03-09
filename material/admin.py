from django.contrib import admin
from material.models import Vehiculo, EAVM
from material.models import SistemaVehiculo, SistemaEAVM 
from material.models import ConjuntoVehiculo, ConjuntoEAVM
from material.models import ComponenteVehiculo, ComponenteEAVM

# Register your models here.
admin.site.register(Vehiculo)
admin.site.register(EAVM)
admin.site.register(SistemaVehiculo)
admin.site.register(SistemaEAVM)
admin.site.register(ConjuntoVehiculo)
admin.site.register(ConjuntoEAVM)
admin.site.register(ComponenteVehiculo)
admin.site.register(ComponenteEAVM)
