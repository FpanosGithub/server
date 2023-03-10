# Generated by Django 4.0.4 on 2023-03-08 15:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('ingenieria', '0001_initial'),
        ('eventos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='registrointervencionsi',
            name='instruccion',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, to='ingenieria.instrucciontecnica'),
        ),
        migrations.AddField(
            model_name='registrointervencionsi',
            name='intervencion',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='eventos.intervencionvehiculo'),
        ),
        migrations.AddField(
            model_name='registrointervencioneavm',
            name='instruccion',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, to='ingenieria.instrucciontecnica'),
        ),
        migrations.AddField(
            model_name='registrointervencioneavm',
            name='intervencion',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='eventos.intervencioneavm'),
        ),
    ]
