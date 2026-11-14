from django.http import HttpResponse
from django.shortcuts import render
from empresa.models import Vaga

def lista_vagas(request):
    vagas = Vaga.objects.all().order_by("-id")

    return render(
        request,
        "vagas/lista_vagas.html",
        {"vagas": vagas}
    )
