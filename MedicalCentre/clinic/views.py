from rest_framework import viewsets
from .models import Clinica, Medico, Paciente, Consulta
from .serializers import ClinicaSerializer, MedicoSerializer, PacienteSerializer, ConsultaSerializer, NestedClinicaSerializer



class ClinicaViewSet(viewsets.ModelViewSet):
    queryset = Clinica.objects.all()

    def get_serializer_class(self):
        if self.action == 'create':
            return NestedClinicaSerializer
        return ClinicaSerializer



class MedicoViewSet(viewsets.ModelViewSet):
    serializer_class = MedicoSerializer
    queryset = Medico.objects.all()


class PacienteViewSet(viewsets.ModelViewSet):
    serializer_class = PacienteSerializer
    queryset = Paciente.objects.all()


class ConsultaViewSet(viewsets.ModelViewSet):
    serializer_class = ConsultaSerializer
    queryset = Consulta.objects.all()
