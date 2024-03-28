from django.db import models
from aluno.models import Aluno as AlunoOriginal

# Create your models here.
class Aluno(AlunoOriginal):
    plus = models.CharField(max_length=100)

    def nomecompleto(self):
        return f"{self.nome} ({self.matricula}) - {self.plus}"

    def nomecompleto_email_plus(self):
        return f"{self.nome} ({self.matricula}) - {self.email} - {self.plus}"
