# Generated by Django 5.1.2 on 2024-12-04 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Reservas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_reserva', models.IntegerField(max_length=10)),
                ('id_huespedes', models.IntegerField(max_length=10)),
                ('id_habitacion', models.IntegerField(max_length=10)),
                ('Fecha_de_Entrada', models.DateField()),
                ('Fecha_de_salida', models.DateField()),
                ('total_pago', models.CharField(max_length=50)),
                ('estado', models.CharField(max_length=20)),
            ],
        ),
    ]