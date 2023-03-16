r"""Models for clinic
Relations:
    Clinica has a one-to-many relation with:
        Medico has a one-to-many relation with:
            Paciente has a one-to-many relation with:
                Consulta
This is just a test for docstring
"""


from django.db import models
from django.contrib import admin
from django.utils import timezone
from django.core.validators import MinValueValidator


class Clinica(models.Model):
    nome_da_clinica = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nome_da_clinica
    
    def __repr__(self) -> str:
        return self.__str__()


class Medico(models.Model):
    nome_do_medico = models.CharField(max_length=100)
    crm = models.CharField(max_length=20)
    clinica = models.ForeignKey(Clinica, on_delete=models.CASCADE, related_name='medicos')
    
    def __str__(self):
        return self.nome_do_medico

    def __repr__(self) -> str:
        return self.__str__()
    

class Paciente(models.Model):
    nome_do_paciente = models.CharField(max_length=100)
    idade_do_paciente = models.IntegerField(validators=[MinValueValidator(0, "Idade deve ser menor que zero")])
    peso_do_paciente = models.DecimalField(decimal_places=2, max_digits=4, validators=[MinValueValidator(0, "Peso deve ser maior que 0")])
    altura_do_paciente = models.DecimalField(decimal_places=2, max_digits=5, validators=[MinValueValidator(0, "Altura deve ser maior que 0")])
    detalhes_do_paciente = models.TextField()
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE, related_name='pacientes')
    
    def __str__(self):
        return self.nome_do_paciente
    
    def __repr__(self) -> str:
        return self.__str__()
    

class Consulta(models.Model):
    motivo_da_consulta = models.CharField(max_length=100)
    data_agendada = models.DateTimeField("Data Agendada")
    detalhes_da_consulta = models.TextField()
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, related_name='consultas')

    def __repr__(self) -> str:
        return self.__str__()
    
    def __str__(self):
        return f"{self.motivo_da_consulta} - {self.paciente.nome_do_paciente}"

    @admin.display(
        boolean=True,
        ordering='pub_date',
        description='Passou da data?'
    )  
    def passou_da_data(self):
        now = timezone.now()
        return self.data_agendada >= now