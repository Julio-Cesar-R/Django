# Generated by Django 4.0.4 on 2022-08-02 01:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_empleados'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Empleados',
            new_name='Empleado',
        ),
        migrations.AlterModelOptions(
            name='empleado',
            options={'verbose_name': 'Empleado', 'verbose_name_plural': 'Empleados'},
        ),
        migrations.AlterModelTable(
            name='empleado',
            table='empleado',
        ),
    ]