from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('red_ferr/', include('red_ferroviaria.urls')),
    path('material/', include('material.urls')),
    path('eventos/', include('eventos.urls')),
    path('streaming/', include('streaming.urls')),
]
