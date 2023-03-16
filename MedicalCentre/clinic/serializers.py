from rest_framework import serializers
from .models import Clinica, Medico, Paciente, Consulta


class ClinicaSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    nome_da_clinica = serializers.CharField(required=True, allow_blank=False, max_length=100)

    def create(self, validated_data):
        return Clinica.objects.create(**validated_data)
    
    def update(self, instance: Clinica, validated_data: dict):
        instance.nome_da_clinica = validated_data.get('nome_da_clinica')
        instance.save()
        return instance
    

# class MedicoSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     nome_do_medico = serializers.CharField(required=True, allow_blank=False, max_length=100)
#     crm = serializers.CharField(required=True, allow_blank=False, max_length=100)

#     def create(self, validated_data):
#         return Medico.objects.create(**validated_data)
    
#     def update(self, instance: Medico, validated_data: dict):
#         instance.nome_do_medico = validated_data.get('nome_do_medico')
#         instance.crm = validated_data.get('crm')
#         instance.save()
#         return instance


# class PacienteSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     nome_do_paciente = serializers.CharField(required=True, allow_blank=False, max_length=100)
#     idade_do_paciente = serializers.IntegerField(required=True, allow_blank=False)
#     peso_do_paciente = serializers.DecimalField(required=True, allow_blank=False)
#     detalhes_do_paciente = serializers.CharField(required=True, allow_blank=False)

#     def create(self, validated_data):
#         return Paciente.objects.create(**validated_data)
    
#     def update(self, instance: Paciente, validated_data: dict):
#         instance.nome_do_paciente = validated_data.get('nome_do_paciente')
#         instance.idade_do_paciente = validated_data.get('idade_do_paciente')
#         instance.peso_do_paciente = validated_data.get('peso_do_paciente')
#         instance.altura_do_paciente = validated_data.get('altura_do_paciente')
#         instance.detalhes_do_paciente = validated_data.get('detalhes_do_paciente')
#         instance.save()
#         return instance