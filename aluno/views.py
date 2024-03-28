from django.shortcuts import render
from cidades.alunocid.models import Aluno  # Alterado aqui para puxar no novo model
from cidades.alunocid.views import homeDecorator  # Alterado aqui para puxar no novo decorator

# Create your views here.
@homeDecorator
def home(request):

    aluno = Aluno.objects.get(pk=3)
    print(aluno.nomecompleto_email())  # Usando método da classe original

    return render(request, 'home.html')
