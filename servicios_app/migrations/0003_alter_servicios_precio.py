# Generated by Django 5.1.2 on 2024-12-06 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servicios_app', '0002_alter_servicios_id_servicio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicios',
            name='precio',
            field=models.CharField(max_length=100),
        ),
    ]