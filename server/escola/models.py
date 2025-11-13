from django.db import models
from django.core.validators import MinLengthValidator


# Create your models here.
class Estudante(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(blank=False, max_length=30)
    cpf = models.CharField(max_length=11, unique=True)
    data_nascimento = models.DateField()
    numero = models.CharField(max_length=14)

    def __str__(self) -> str:
        return f"{self.pk} - {self.nome}"


class Curso(models.Model):
    codigo = models.CharField(max_length=10,unique=True, validators=[MinLengthValidator(4)])
    descricao = models.TextField(blank=False)
    NIVEL_CHOICES = (
        ("B", "Básico"),
        ("I", "Intermediário"),
        ("A", "Avançado"),
    )
    nivel = models.CharField(
        max_length=1, choices=NIVEL_CHOICES, blank=False, null=False, default="B"
    )

    def __str__(self):
        return f"{self.pk} - {self.descricao}"


class Matricula(models.Model):
    PERIODO = (
        ("M", "Matutino"),
        ("V", "Vespertino"),
        ("N", "Noturno"),
    )
    estudante = models.ForeignKey(Estudante, on_delete=models.CASCADE, null=False)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, null=False)
    periodo = models.CharField(choices=PERIODO, null=False, default="M", max_length=1)
