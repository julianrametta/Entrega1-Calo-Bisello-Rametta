# Generated by Django 4.0.4 on 2022-06-01 01:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('familia', '0006_delete_mascota'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mascota',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=100)),
                ('raza', models.CharField(max_length=100)),
                ('nombre', models.CharField(max_length=100)),
                ('fecha_nacimiento', models.DateField()),
            ],
        ),
    ]
