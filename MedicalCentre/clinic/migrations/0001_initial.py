# Generated by Django 4.1.7 on 2023-02-28 21:00

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Clinica',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_da_clinica', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Medico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('crm', models.CharField(max_length=20)),
                ('clinica', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clinic.clinica')),
            ],
        ),
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_do_paciente', models.CharField(max_length=100)),
                ('idade_do_paciente', models.IntegerField(validators=[django.core.validators.MinValueValidator(0, 'Idade deve ser menor que zero')])),
                ('peso_do_paciente', models.DecimalField(decimal_places=2, max_digits=4, validators=[django.core.validators.MinValueValidator(0, 'Peso deve ser maior que 0')])),
                ('altura_do_paciente', models.DecimalField(decimal_places=2, max_digits=5, validators=[django.core.validators.MinValueValidator(0, 'Altura deve ser maior que 0')])),
                ('detalhes_do_paciente', models.TextField()),
                ('medico', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clinic.medico')),
            ],
        ),
        migrations.CreateModel(
            name='Consulta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('motivo_da_consulta', models.CharField(max_length=100)),
                ('data_agendada', models.DateTimeField(verbose_name='Data Agendada')),
                ('detalhes_da_consulta', models.TextField()),
                ('paciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clinic.paciente')),
            ],
        ),
    ]
