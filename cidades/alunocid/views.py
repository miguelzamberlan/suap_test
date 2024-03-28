from django.shortcuts import render
from cidades.alunocid.models import Aluno
from functools import wraps

# Create your views here.
def homeDecorator(func):
    @wraps(func)
    def wrapper(request, *args, **kwargs):

        result = func(request, *args, **kwargs)

        print("Novas funcionalidades aqui!")

        return result

    return wrapper


"""
Outra opção
Este método substitui o método original da classe Aluno
"""
# Alterar o arquivo urls.py para apontar para a nova view que também terá o nome de home
def home(request):
    aluno = Aluno.objects.get(pk=3)
    print(aluno.nomecompleto_email())  # Usando método da classe original
    print(aluno.nomecompleto())  # Reescrita do método
    print(aluno.nomecompleto_email_plus())  # Usando método da classe nova que não tem na original

    return render(request, 'home.html')

# OBSEVAÇÃO:
# No banco de dados mantem a tabela original e cria uma nova tabela com os adicionais
# Como substituir um método da view sem alterar o código fonte original ?
