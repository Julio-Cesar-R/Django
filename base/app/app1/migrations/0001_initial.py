# Generated by Django 4.0.4 on 2022-06-06 04:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Demostracion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dato1', models.CharField(max_length=50, verbose_name='Dato1')),
                ('dato2', models.CharField(max_length=50, verbose_name='Dato2')),
                ('dato3', models.CharField(blank=True, max_length=120, verbose_name='Dato3')),
            ],
            options={
                'verbose_name': 'Demostracion',
                'verbose_name_plural': 'Demostraciones',
                'ordering': ['id'],
            },
        ),
    ]
