# Generated by Django 5.1.2 on 2024-12-05 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facturacion_app', '0002_facturacion_monto_total'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='facturacion',
            name='id',
        ),
        migrations.AlterField(
            model_name='facturacion',
            name='id_factura',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]