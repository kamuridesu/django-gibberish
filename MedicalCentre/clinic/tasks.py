r"""This file will hold as many tasks as possible for each method"""

from celery import shared_task
from .models import Clinica, Medico, Paciente, Consulta


@shared_task
def create_nested_objects(validated_data):
    print(validated_data)
    medicos_data = validated_data.pop('medicos')
    clinica = Clinica.objects.create(**validated_data)
    for medico_data in medicos_data:
        if "pacientes" in medico_data:
            pacientes_data = medico_data.pop('pacientes')
            for paciente_data in pacientes_data:
                if "consultas" in paciente_data:
                    consultas_data = paciente_data.pop('consultas')
                    for consulta_data in consultas_data:
                        Consulta.objects.create(paciente=consulta_data.pop("paciente"), **consulta_data)
                paciente = Paciente.objects.create(medico=paciente_data.pop("medico"), **paciente_data)
        medico = Medico.objects.create(clinica=medico_data.pop("clinica"), **medico_data)
        
    return clinica
