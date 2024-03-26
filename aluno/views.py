from django.shortcuts import render
from aluno.models import Aluno

# Create your views here.
def home(request):
    # aluno = Aluno.objects.all()
    # print(aluno)
    print(Aluno)

    return render(request, 'home.html')
