# Generated by Django 5.1.2 on 2024-12-05 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facturacion_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='facturacion',
            name='monto_total',
            field=models.CharField(default='100', max_length=100),
        ),
    ]
