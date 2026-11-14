from django.http import HttpResponse
from django.shortcuts import render, redirect
from empresa.models import Vaga
from django.contrib import messages
from .forms import VagaForm

def lista_vagas(request):
    vagas = Vaga.objects.all().select_related("empresa")

    return render(
        request,
        "vagas/lista_vagas.html",
        {"vagas": vagas}
    )


def cadastrar_vaga(request):

    if request.method == "POST":
        form = VagaForm(
            request.POST,
            usuario=request.user
        )

        if form.is_valid():
            vaga = form.save()

            messages.success(
                request,
                "Vaga cadastrada com sucesso!"
            )

            return redirect("vagas:lista")

    else:
        form = VagaForm()

    return render(
        request,
        "vagas/cadastrar_vaga.html",
        {"form": form}
    )

