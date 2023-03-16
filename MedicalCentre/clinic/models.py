from django.db import models
from django.contrib import admin
from django.utils import timezone
from django.core.validators import MinValueValidator


class Clinica(models.Model):
    nome_da_clinica = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.nome_da_clinica
    
    def __repr__(self) -> str:
        return self.__str__()


class Medico(models.Model):
    clinica = models.ForeignKey(Clinica, on_delete=models.CASCADE) 
    crm = models.CharField(max_length=20)

    def __str__(self) -> str:
        return self.nome_do_medico
    
    def __repr__(self) -> str:
        return self.__str__()


class Paciente(models.Model):
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE)
    nome_do_paciente = models.CharField(max_length=100)
    idade_do_paciente = models.IntegerField(validators=[MinValueValidator(0, "Idade deve ser menor que zero")])
    peso_do_paciente = models.DecimalField(decimal_places=2, max_digits=4, validators=[MinValueValidator(0, "Peso deve ser maior que 0")])
    altura_do_paciente = models.DecimalField(decimal_places=2, max_digits=5, validators=[MinValueValidator(0, "Altura deve ser maior que 0")])
    detalhes_do_paciente = models.TextField()

    def __str__(self) -> str:
        return self.nome_do_paciente
    
    def __repr__(self) -> str:
        return self.__str__()


class Consulta(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    motivo_da_consulta = models.CharField(max_length=100)
    data_agendada = models.DateTimeField("Data Agendada")
    detalhes_da_consulta = models.TextField()

    @admin.display(
        boolean=True,
        ordering='pub_date',
        description='Passou da data?'
    )
    def passou_da_data(self):
        now = timezone.now()
        return self.data_agendada >= now

    def __str__(self) -> str:
        return self.motivo_da_consulta
    
    def __repr__(self) -> str:
        return self.__str__()
