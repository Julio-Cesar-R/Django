# Generated by Django 4.0.4 on 2022-05-27 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('persona', '0002_habilidad_alter_empleado_options_empleado_image_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='empleado',
            name='habilidades',
            field=models.ManyToManyField(to='persona.habilidad'),
        ),
    ]
