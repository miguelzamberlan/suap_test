from django.db import models

# Create your models here.
class Aluno(models.Model):
    nome = models.CharField(max_length=100)
    matricula = models.CharField(max_length=20)
    email = models.EmailField()
    telefone = models.CharField(max_length=20)
    data_nascimento = models.DateField()
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def nomecompleto(self):
        return f"{self.nome} ({self.matricula})"

    def nomecompleto_email(self):
        return f"{self.nome} ({self.matricula}) - {self.email}"

    def __str__(self):
        return self.nome
