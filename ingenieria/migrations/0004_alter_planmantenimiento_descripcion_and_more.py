# Generated by Django 4.1.7 on 2023-03-13 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ingenieria', '0003_remove_instrucciontecnica_slug_it_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='planmantenimiento',
            name='descripcion',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='tipovehiculo',
            name='tipo_uic',
            field=models.CharField(blank=True, max_length=2, null=True),
        ),
    ]
