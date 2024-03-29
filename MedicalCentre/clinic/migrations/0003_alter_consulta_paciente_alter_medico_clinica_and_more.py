# Generated by Django 4.1.7 on 2023-03-15 22:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("clinic", "0002_medico_nome_do_medico"),
    ]

    operations = [
        migrations.AlterField(
            model_name="consulta",
            name="paciente",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="consultas",
                to="clinic.paciente",
            ),
        ),
        migrations.AlterField(
            model_name="medico",
            name="clinica",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="medicos",
                to="clinic.clinica",
            ),
        ),
        migrations.AlterField(
            model_name="paciente",
            name="medico",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="pacientes",
                to="clinic.medico",
            ),
        ),
    ]
