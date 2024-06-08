# Generated by Django 5.0.3 on 2024-06-08 03:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EF',
            fields=[
                ('id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('pielymucosa', models.CharField(max_length=50)),
                ('tcs', models.CharField(max_length=50)),
                ('mamas', models.CharField(max_length=50)),
                ('acv', models.CharField(max_length=50)),
                ('abdomen', models.CharField(max_length=50)),
                ('snc', models.CharField(max_length=50)),
                ('soma', models.CharField(max_length=50)),
                ('genitalesexternos', models.CharField(max_length=50)),
                ('conducta', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='EM',
            fields=[
                ('id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('edad', models.CharField(max_length=50)),
                ('sexi', models.CharField(max_length=50)),
                ('appersonales', models.CharField(max_length=50)),
                ('apfamiliares', models.CharField(max_length=50)),
                ('vicio', models.CharField(max_length=50)),
                ('opreciones', models.CharField(max_length=50)),
                ('transfuciones', models.CharField(max_length=50)),
                ('vacunacion', models.CharField(max_length=50)),
                ('alergico', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Enfermedad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Grupos',
            fields=[
                ('nombre', models.CharField(max_length=50, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('nombre', models.CharField(max_length=50)),
                ('apellidos', models.CharField(max_length=50)),
                ('ci', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('telefono', models.CharField(max_length=50)),
                ('direccion', models.CharField(max_length=50)),
                ('ocupacion', models.CharField(max_length=50)),
                ('grupos', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pacientes', to='Historia.grupos')),
            ],
        ),
        migrations.CreateModel(
            name='Historial',
            fields=[
                ('id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('fecha', models.CharField(max_length=50)),
                ('ef', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='historial', to='Historia.ef')),
                ('em', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='historial', to='Historia.em')),
                ('enfermedad', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='historial', to='Historia.enfermedad')),
                ('paciente', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='historial', to='Historia.paciente')),
            ],
        ),
    ]
