# Generated by Django 4.1.7 on 2023-03-13 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('material', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehiculo',
            name='descripcion_particular',
            field=models.CharField(blank=True, default='', max_length=100, null=True),
        ),
    ]
