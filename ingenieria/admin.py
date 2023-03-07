from django.contrib import admin
from ingenieria.models import TipoVehiculo, SistemasVehiculo, EjesVehiculo
from ingenieria.models import Sistema, Componente, ITM
from ingenieria.models import TipoEje, TipoConjuntoEje, TipoElementoEje, ConsistenciaEje
from ingenieria.models import VersionCambiador

# Register your models here.
admin.site.register(TipoVehiculo)
admin.site.register(Sistema)
admin.site.register(Componente)
admin.site.register(ITM)

admin.site.register(TipoEje)
admin.site.register(TipoConjuntoEje)
admin.site.register(TipoElementoEje)
admin.site.register(ConsistenciaEje)

admin.site.register(SistemasVehiculo)
admin.site.register(EjesVehiculo)

admin.site.register(VersionCambiador)