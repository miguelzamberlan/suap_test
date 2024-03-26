from django.db import models
from aluno.models import Aluno as AlunoOriginal

# Create your models here.
class Aluno(AlunoOriginal):
    plus = models.CharField(max_length=100)
