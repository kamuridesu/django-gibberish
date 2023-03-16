from rest_framework import serializers
from .models import Clinica, Medico, Paciente, Consulta
from .tasks import create_nested_objects

from pprint import pprint


class ConsultaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consulta
        fields = '__all__'


class PacienteSerializer(serializers.ModelSerializer):
    consultas = ConsultaSerializer(many=True, read_only=True)

    class Meta:
        model = Paciente
        fields = '__all__'


class MedicoSerializer(serializers.ModelSerializer):
    pacientes = PacienteSerializer(many=True, read_only=True)

    class Meta:
        model = Medico
        fields = '__all__'


class NestedConsultaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consulta
        fields = '__all__'


class NestedPacienteSerializer(serializers.ModelSerializer):
    consultas = NestedConsultaSerializer(many=True)

    class Meta:
        model = Paciente
        fields = '__all__'


class NestedMedicoSerializer(serializers.ModelSerializer):
    pacientes = NestedPacienteSerializer(many=True)

    class Meta:
        model = Medico
        fields = '__all__'


class NestedClinicaSerializer(serializers.ModelSerializer):
    medicos = NestedMedicoSerializer(many=True)

    class Meta:
        model = Clinica
        fields = '__all__'

    def create(self, validated_data):
        clinica = create_nested_objects.delay(validated_data)
        return self.to_representation(clinica.get())

class ClinicaSerializer(serializers.ModelSerializer):
    medicos = MedicoSerializer(many=True, read_only=True)

    class Meta:
        model = Clinica
        fields = '__all__'

