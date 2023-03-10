# Generated by Django 4.0.4 on 2023-03-08 15:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('organizaciones', '0001_initial'),
        ('ingenieria', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Linea',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=16, unique=True)),
                ('nombre', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PuntoRed',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=16, unique=True)),
                ('descripcion', models.CharField(blank=True, max_length=100, null=True)),
                ('nudo', models.BooleanField(default=False)),
                ('pkilometrico', models.FloatField(blank=True, null=True)),
                ('lng', models.FloatField(default=-3.982)),
                ('lat', models.FloatField(default=40.2951)),
                ('linea', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, to='red_ferroviaria.linea')),
            ],
        ),
        migrations.CreateModel(
            name='Cambiador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=16, unique=True)),
                ('nombre', models.CharField(default='Experimental-01', max_length=100)),
                ('fecha_fab', models.DateField(blank=True, null=True)),
                ('num_cambios', models.IntegerField(default=0)),
                ('mantenimiento', models.CharField(blank=True, max_length=16, null=True)),
                ('lng', models.FloatField(default=-4.692)),
                ('lat', models.FloatField(default=37.9246)),
                ('EEM', models.ForeignKey(blank=True, limit_choices_to={'de_cambiadores': True}, null=True, on_delete=django.db.models.deletion.RESTRICT, to='organizaciones.eem')),
                ('fabricante', models.ForeignKey(blank=True, limit_choices_to={'de_cambiadores': True}, null=True, on_delete=django.db.models.deletion.RESTRICT, to='organizaciones.fabricante')),
                ('version', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, to='ingenieria.versioncambiador')),
            ],
        ),
    ]
