from django.contrib import admin
from ingenieria.models import PlanMantenimiento, NivelesPlan, InstruccionTecnica
from ingenieria.models import TipoVehiculo, TipoEAVM, SistemasVehiculo, SistemasEAVM
from ingenieria.models import TipoSistema, TipoConjunto, TipoComponente
from ingenieria.models import VersionCambiador

# Register your models here.
admin.site.register(PlanMantenimiento)
admin.site.register(NivelesPlan)
admin.site.register(InstruccionTecnica)
admin.site.register(TipoVehiculo)
admin.site.register(TipoEAVM)
admin.site.register(SistemasVehiculo)
admin.site.register(SistemasEAVM)
admin.site.register(TipoSistema)
admin.site.register(TipoConjunto)
admin.site.register(TipoComponente)
admin.site.register(VersionCambiador)