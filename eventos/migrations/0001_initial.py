# Generated by Django 4.0.4 on 2023-03-08 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AlarmaCambiador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activa', models.BooleanField(default=False)),
                ('dt', models.DateTimeField(blank=True, null=True)),
                ('tipo', models.CharField(choices=[('OPERACION', 'OPERACION'), ('GENERAL', 'GENERAL'), ('MANTENIMIENTO', 'MANTENIMIENTO')], default='OPERACION', max_length=15)),
                ('mensaje', models.CharField(blank=True, max_length=50, null=True)),
                ('informe_solucion', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='AlarmaEAVM',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activa', models.BooleanField(default=False)),
                ('dt', models.DateTimeField(blank=True, null=True)),
                ('tipo', models.CharField(choices=[('TEMPERATURA', 'TEMPERATURA'), ('CIRCULACION', 'CIRCULACION'), ('CAMBIO', 'CAMBIO'), ('MANTENIMIENTO', 'MANTENIMIENTO')], default='CIRCULACION', max_length=15)),
                ('mensaje', models.CharField(blank=True, max_length=50, null=True)),
                ('informe_solucion', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='AlarmaVehiculo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activa', models.BooleanField(default=False)),
                ('dt', models.DateTimeField(blank=True, null=True)),
                ('tipo', models.CharField(choices=[('TRANSMISION', 'TRANSMISION'), ('CIRCULACION', 'CIRCULACION'), ('MANTENIMIENTO', 'MANTENIMIENTO')], default='CIRCULACION', max_length=15)),
                ('mensaje', models.CharField(blank=True, max_length=50, null=True)),
                ('informe_solucion', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='CambioEAVM',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num_cambio_EAVM', models.IntegerField(default=0)),
                ('alarma', models.BooleanField(default=False)),
                ('inicio', models.DateTimeField()),
                ('V', models.FloatField(default=2.77)),
                ('FV', models.FloatField(default=250)),
                ('tdaM', models.FloatField(default=5000)),
                ('fdaM', models.FloatField(default=30)),
                ('ddaM', models.FloatField(default=10)),
                ('tcaM', models.FloatField(default=10000)),
                ('fcaM', models.FloatField(default=20)),
                ('dcaM', models.FloatField(default=70)),
                ('team', models.FloatField(default=15000)),
                ('feam', models.FloatField(default=10)),
                ('deam', models.FloatField(default=20)),
                ('tdbM', models.FloatField(default=25000)),
                ('fdbM', models.FloatField(default=30)),
                ('ddbM', models.FloatField(default=10)),
                ('tcbM', models.FloatField(default=300000)),
                ('fcbM', models.FloatField(default=20)),
                ('dcbM', models.FloatField(default=70)),
                ('tebm', models.FloatField(default=35000)),
                ('febm', models.FloatField(default=10)),
                ('debm', models.FloatField(default=20)),
            ],
        ),
        migrations.CreateModel(
            name='CirculacionEAVM',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('abierta', models.BooleanField(default=True)),
                ('dt_inicial', models.DateTimeField()),
                ('lat_inicial', models.FloatField(default=-3.982)),
                ('lng_inicial', models.FloatField(default=40.2951)),
                ('punto_red_inicial', models.CharField(blank=True, max_length=16, null=True)),
                ('dt_final', models.DateTimeField(blank=True, null=True)),
                ('lat_final', models.FloatField(default=-3.982)),
                ('lng_final', models.FloatField(default=40.2951)),
                ('punto_red_final', models.CharField(blank=True, max_length=16, null=True)),
                ('alarma', models.BooleanField(blank=True, default=False, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='CirculacionVehiculo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('abierta', models.BooleanField(default=True)),
                ('dt_inicial', models.DateTimeField()),
                ('lat_inicial', models.FloatField(default=-3.982)),
                ('lng_inicial', models.FloatField(default=40.2951)),
                ('punto_red_inicial', models.CharField(blank=True, max_length=16, null=True)),
                ('dt_final', models.DateTimeField(blank=True, null=True)),
                ('lat_final', models.FloatField(default=-3.982)),
                ('lng_final', models.FloatField(default=40.2951)),
                ('punto_red_final', models.CharField(blank=True, max_length=16, null=True)),
                ('alarma', models.BooleanField(blank=True, default=False, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='EventoEAVM',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dt', models.DateTimeField()),
                ('lng', models.FloatField(default=-3.982)),
                ('lat', models.FloatField(default=40.2951)),
                ('evento', models.CharField(blank=True, choices=[('START', 'EMPIEZA'), ('STOP', 'PARA'), ('CIRC', 'CIRCULANDO'), ('NUDO', 'NUDO'), ('CAMBIO', 'CAMBIO')], default='CIRC', max_length=12, null=True)),
                ('vel', models.FloatField(blank=True, default=0, null=True)),
                ('tempa', models.FloatField(blank=True, default=25, null=True)),
                ('tempb', models.FloatField(blank=True, default=25, null=True)),
                ('alarma', models.BooleanField(blank=True, default=False, null=True)),
                ('axMa', models.FloatField(blank=True, default=2.5, null=True)),
                ('axMb', models.FloatField(blank=True, default=2.5, null=True)),
                ('ayMa', models.FloatField(blank=True, default=3.5, null=True)),
                ('ayMb', models.FloatField(blank=True, default=3.5, null=True)),
                ('azMa', models.FloatField(blank=True, default=4.5, null=True)),
                ('azMb', models.FloatField(blank=True, default=4.5, null=True)),
                ('axmeda', models.FloatField(blank=True, default=2.5, null=True)),
                ('axmedb', models.FloatField(blank=True, default=2.5, null=True)),
                ('aymeda', models.FloatField(blank=True, default=3.5, null=True)),
                ('aymedb', models.FloatField(blank=True, default=3.5, null=True)),
                ('azmeda', models.FloatField(blank=True, default=4.5, null=True)),
                ('azmedb', models.FloatField(blank=True, default=4.5, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='EventoVehiculo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dt', models.DateTimeField()),
                ('lng', models.FloatField(default=-3.982)),
                ('lat', models.FloatField(default=40.2951)),
                ('evento', models.CharField(blank=True, choices=[('START', 'EMPIEZA'), ('STOP', 'PARA'), ('CIRC', 'CIRCULANDO'), ('NUDO', 'NUDO')], default='CIRC', max_length=12, null=True)),
                ('vel', models.FloatField(blank=True, default=0, null=True)),
                ('alarma', models.BooleanField(blank=True, default=False, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='IntervencionEAVM',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nivel', models.CharField(blank=True, max_length=5, null=True)),
                ('inicio', models.DateField(blank=True, null=True)),
                ('fin', models.DateField(blank=True, null=True)),
                ('km', models.FloatField(default=0)),
                ('firmado_por', models.CharField(blank=True, max_length=25, null=True)),
                ('supervisado_por', models.CharField(blank=True, max_length=25, null=True)),
                ('NC', models.BooleanField(default=False)),
                ('NoConformidad', models.CharField(blank=True, max_length=15, null=True)),
                ('cerrada', models.BooleanField(default=True)),
                ('apta', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='IntervencionVehiculo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nivel', models.CharField(blank=True, max_length=5, null=True)),
                ('inicio', models.DateField(blank=True, null=True)),
                ('fin', models.DateField(blank=True, null=True)),
                ('km', models.FloatField(default=0)),
                ('firmado_por', models.CharField(blank=True, max_length=25, null=True)),
                ('supervisado_por', models.CharField(blank=True, max_length=25, null=True)),
                ('NC', models.BooleanField(default=False)),
                ('NoConformidad', models.CharField(blank=True, max_length=15, null=True)),
                ('cerrada', models.BooleanField(default=True)),
                ('apta', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Noticia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('titulo', models.CharField(blank=True, max_length=50, null=True)),
                ('mensaje', models.CharField(blank=True, max_length=250, null=True)),
                ('foto', models.CharField(blank=True, max_length=16, null=True)),
                ('subproyecto', models.CharField(choices=[('Ejes', 'Ejes'), ('Cambiador', 'Cambiador'), ('Vagones', 'Vagones'), ('Banco Tria', 'Banco Tria'), ('Banco C??rdoba', 'Banco C??rdoba')], default='Ejes', max_length=15)),
                ('alerta', models.BooleanField(default=False)),
                ('logro', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='OperacionCambio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dt', models.DateTimeField()),
                ('sentido', models.CharField(choices=[('UICIB', 'UIC->IB'), ('IBUIC', 'IB->UIC'), ('UICRUS', 'UIC->RUS'), ('RUSUIC', 'RUS->UIC')], default='UICIB', max_length=8)),
                ('alarma', models.BooleanField(default=False)),
                ('alarma_activa', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='RegistroIntervencionEAVM',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='RegistroIntervencionSI',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]
